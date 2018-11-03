# Written by Eric Martin for COMP9021


from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.filedialog


BACKGROUND_COLOUR = '#FAF5F3'
LINE_COLOUR = '#115523'
SPACE = 15


class Maze(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Simple, alternating transit mazes')
        menubar = Menu()
        help_menu = Menu(menubar)
        menubar.add_cascade(label = 'Maze Help', menu = help_menu)
        help_menu.add_command(label = 'Input', command = self.input_help)
        help_menu.add_command(label = 'S.a.t. mazes', command = self.sat_mazes_help)
        help_menu.add_command(label = 'Output', command = self.output_help)
        self.config(menu = menubar)
        
        Label(self, text = 'Level sequence: ').grid(sticky = E, padx = 5, pady = 20)
        self.input = Entry(self, width = 36)
        self.input.grid(row = 0, column = 1, sticky = W)
        self.shown_level_sequence = StringVar()
        Label(self, width = 70, height = 1, textvariable = self.shown_level_sequence, fg = 'magenta').grid(columnspan = 2, pady = 20)
        self.maze = Canvas(self, width = 40 * SPACE, height = 40 * SPACE, bg = BACKGROUND_COLOUR)
        self.maze.grid(columnspan = 2, padx = 20)
        Button(self, text = 'Display maze', command = self.display_maze).grid(pady = 20)
        latex_code_button = Button(self, text = 'Save Latex code', command = self.save_latex_code).grid(row = 3, column = 1)
        self.displayed_maze = False

    def input_help(self):
        tkinter.messagebox.showinfo('Input',
            'The input should be a permutation of all numbers from 0 to N '
            'with N between 3 and 19, that forms a level sequence, that is:\n'
            ' - starts with 0 and ends in N\n'
            ' - alternates between even and odd numbers\n'
            ' - is such that for all pairs of successive numbers '
            '(p1, p2) and (q1, q2) with p1 and q1 of the same parity '
            '(and so also p2 and q2 of the same parity), the intervals '
            '[p1, p2] and [q1, q2] are disjoint or one is included in the other.')

    def sat_mazes_help(self):
        tkinter.messagebox.showinfo('S.a.t. mazes',
            'See http://www.math.sunysb.edu/~tony/mazes/ '
            'for a description of simple, aternative transit (s.a.t.) mazes, '
            'and in particular the proof of necessity and sufficiency '
            'for a permutation of the numbers from 0 to N to be the level sequence '
            'of an s.a.t. maze of depth N, from which the current implementation is derived.')

    def output_help(self):
        tkinter.messagebox.showinfo('Output',
            'If some input has been provided and the user clicks on either button, '
            'then the input is checked for validity and in case it is valid, '
            'the maze determined by the input is displayed; moreover, in case '
            'the user has clicked on the "Save Latex code" button then Latex code '
            'for that maze is generated and saved.\n\n'
            'In case the user clicks on the "Save Latex code" button, '
            'a maze is been displayed and no new input has been provided, '
            'then Latex code for the displayed maze is generated and saved.')

    def display_maze(self, input = None):
        if not input:
            input = self.input.get()
            if not input:
                return
        input = self.get_level_sequence(input)
        if not input:
            self.displayed_maze = False
            return
        self.shown_level_sequence.set('Level sequence ' + str(self.level_sequence))
        self.complete_pairs_and_depths(self.left_pairs, self.left_depths)
        self.complete_pairs_and_depths(self.right_pairs, self.right_depths)
        self.maze.delete(ALL)
        self.draw_maze('screen')
        self.displayed_maze = True

    def save_latex_code(self):
        input = self.input.get()
        if input:
            self.display_maze(input)
        if self.displayed_maze:
            self.generate_latex_code()

    def generate_latex_code(self):
        filename = tkinter.filedialog.asksaveasfilename(defaultextension='.tex')
        if filename:
            latex_file = open(filename, 'w')
            print('\\documentclass[10pt]{article}',
                  '\\usepackage{tikz}',
                  '\\pagestyle{empty}',
                  '',
                  '\\begin{document}',
                  '',
                  '\\vspace*{\\fill}',
                  '\\begin{center}',
                  '\\begin{tikzpicture}[scale = 1.5, x = 0.25cm, y = -0.25cm, thick, purple]', sep = '\n', file = latex_file)
            self.draw_maze(latex_file)
            print('\\end{tikzpicture}',
                  '\\end{center}',
                  '\\vspace*{\\fill}',
                  '',
                  '\\end{document}', sep = '\n', file = latex_file)
            latex_file.close()

    def get_level_sequence(self, input):
        self.input.delete(0, END)
        try:
            self.level_sequence = list(map(int, input.split()))
        except:
            tkinter.messagebox.showinfo('Input',
            'The input should consist of numbers.')
            return False
        self.max_level = len(self.level_sequence) - 1
        if not 2 < self.max_level < 20:
            tkinter.messagebox.showinfo('Input',
            'The input should consist of between 4 and 20 numbers.')
            return False
        if sorted(self.level_sequence) != list(range(len(self.level_sequence))):
            tkinter.messagebox.showinfo('Input',
            'The input should consist of 0, 1, 2... N, in some order.')
            return False
        if self.level_sequence[0] != 0 or self.level_sequence[self.max_level] != self.max_level:
            tkinter.messagebox.showinfo('Input',
            'The input should start with 0 and end with the largest number.')
            return False
        for i in range(len(self.level_sequence)):
            if self.level_sequence[i] % 2 != i % 2:
                tkinter.messagebox.showinfo('Input',
                'The input should alternate between even and odd numbers.')
                return False
        self.left_pairs = {}
        for i in range(0, self.max_level - 1 + self.max_level % 2, 2):
            self.left_pairs[self.level_sequence[i]] = self.level_sequence[i + 1]
        self.right_pairs = {}
        for i in range(1, self.max_level - self.max_level % 2, 2):
            self.right_pairs[self.level_sequence[i]] = self.level_sequence[i + 1]
        self.left_depths = {0 : 0}
        self.right_depths = {1 : 0}
        if not self.well_balanced(self.left_pairs, self.left_depths) or not self.well_balanced(self.right_pairs, self.right_depths):
            tkinter.messagebox.showinfo('Input', 'The input defines overlapping pairs.')
            return False
        return True

    def well_balanced(self, pairs, depths):
        level_sequence = []
        for i in sorted(pairs.keys()):
            level_sequence.extend([i, pairs[i]])
        shift = 0
        if level_sequence[0]:
            shift = 1
            level_sequence = list(map(lambda x: x - 1, level_sequence))
        for i in range(0, len(level_sequence), 2):
            level_sequence[pairs[i + shift] - shift] = i
        stack = [level_sequence[0]]
        for i in range(1, len(level_sequence)):
            if not stack or stack[-1] != level_sequence[i]:
                depths[i + shift] = len(stack)
                stack.append(level_sequence[i])
            else:
                stack.pop()
        return stack == []

    def complete_pairs_and_depths(self, pairs, depths):
        keys = list(pairs.keys())
        for i in keys:
            pairs[pairs[i]] = i
            if i in depths:
                depths[pairs[i]] = depths[i]
            else:
               depths[i] = depths[pairs[i]]

    def draw_maze(self, where):
        if self.max_level % 2:
            self.draw_line(where, 0, 0, self.max_level - 1, 0)
            self.draw_line(where, self.max_level, 0, 2 * self.max_level, 0)
            for i in range(1, self.max_level - 1):
                if self.left_depths[i] == self.left_depths[i + 1] and self.left_pairs[i] != i + 1:
                    j = self.max_level - self.left_depths[i]
                else:
                    j = max(self.max_level - self.left_depths[i] - 1, self.max_level - self.left_depths[i + 1] - 1)
                if i < j:
                    self.draw_line(where, i, i, j, i)
                if self.right_depths[i] == self.right_depths[i + 1] and self.right_pairs[i] != i + 1:
                    j = self.max_level + self.right_depths[i]
                else:
                    j = min(self.max_level + self.right_depths[i] + 1, self.max_level + self.right_depths[i + 1] + 1)
                if j < 2 * self.max_level - i:
                    self.draw_line(where, j, i, 2 * self.max_level - i, i)
            self.draw_line(where, self.max_level, self.max_level - 1, self.max_level + 1, self.max_level - 1)
            for i in range(self.max_level):
                self.draw_line(where, self.max_level - i - 1, self.max_level + i, self.max_level + i + 1, self.max_level + i)
            for i in self.left_pairs:
                if self.left_pairs[i] < i or self.left_pairs[i] == i + 1:
                    continue
                self.draw_line(where, self.max_level - self.left_depths[i] - 1, i, self.max_level - self.left_depths[i] - 1, self.left_pairs[i] - 1)
            self.draw_line(where, self.max_level, 0, self.max_level, self.max_level - 1)
            for i in self.right_pairs:
                if self.right_pairs[i] < i or self.right_pairs[i] == i + 1:
                    continue
                self.draw_line(where, self.max_level + self.right_depths[i] + 1, i, self.max_level + self.right_depths[i] + 1, self.right_pairs[i] - 1)
            for i in range(self.max_level):
                self.draw_line(where, i, i, i, 2 * self.max_level - i - 1)
                self.draw_line(where, 2 * self.max_level - i, i, 2 * self.max_level - i, 2 * self.max_level - i - 1)
        else:
            self.draw_line(where, 0, 0, self.max_level - 2, 0)
            self.draw_line(where, self.max_level - 1, 0, 2 * self.max_level - 1, 0)
            for i in range(1, self.max_level - 1):
                if self.left_depths[i] == self.left_depths[i + 1] and self.left_pairs[i] != i + 1:
                    j = self.max_level - self.left_depths[i] - 1
                else:

                    j = max(self.max_level - self.left_depths[i] - 2 , self.max_level - self.left_depths[i + 1] - 2)
                if i < j:
                    self.draw_line(where, i, i, j, i)
                if self.right_depths[i] == self.right_depths[i + 1] and self.right_pairs[i] != i + 1:
                    j = self.max_level + self.right_depths[i] - 1
                else:
                    j = min(self.max_level + self.right_depths[i], self.max_level + self.right_depths[i + 1])
                if j < 2 * self.max_level - i - 1:
                    self.draw_line(where, j, i, 2 * self.max_level - i - 1, i)
            for i in range(self.max_level):
                self.draw_line(where, self.max_level - i - 1, self.max_level + i - 1, self.max_level + i, self.max_level + i - 1)
            for i in self.left_pairs:
                  if self.left_pairs[i] < i or self.left_pairs[i] == i + 1:
                     continue
                  self.draw_line(where, self.max_level - self.left_depths[i] - 2, i, self.max_level - self.left_depths[i] - 2, self.left_pairs[i] - 1)
            self.draw_line(where, self.max_level - 1, 0, self.max_level - 1, self.max_level - 1)
            for i in self.right_pairs:
                if self.right_pairs[i] < i or self.right_pairs[i] == i + 1:
                    continue
                self.draw_line(where, self.max_level + self.right_depths[i], i, self.max_level + self.right_depths[i], self.right_pairs[i] - 1)
            for i in range(self.max_level - 1):
                self.draw_line(where, i, i, i, 2 * self.max_level - i - 2)
                self.draw_line(where, 2 * self.max_level - i - 1, i, 2 * self.max_level - i - 1, 2 * self.max_level - i - 2)

    def draw_line(self, where, i1, j1, i2, j2):
        if where == 'screen':
            if self.max_level % 2:
                width = 2 * self.max_level
                height = 2 * self.max_level - 1
            else:
                width = 2 * self.max_level - 1
                height = 2 * self.max_level - 2       
            width_offset = (40 - width) * SPACE / 2
            height_offset = (40 - height) * SPACE / 2
            self.maze.create_line(i1 * SPACE + width_offset, j1 * SPACE + height_offset,
                                  i2 * SPACE + width_offset, j2 * SPACE + height_offset,
                                  width = 0.5, fill = LINE_COLOUR)
        else:
            print('\draw(', i1, ', ', j1, ') -- (', i2, ', ', j2, ');', sep = '', file = where)
                        

        
if __name__ == '__main__':
    Maze().mainloop()
