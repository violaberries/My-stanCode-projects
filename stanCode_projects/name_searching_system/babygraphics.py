"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    space = (width-GRAPH_MARGIN_SIZE*2)//len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index*space
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE,
                       fill='black', width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, fill='black', width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE+((CANVAS_WIDTH-GRAPH_MARGIN_SIZE)/len(YEARS))*i, 0,
                           GRAPH_MARGIN_SIZE+((CANVAS_WIDTH-GRAPH_MARGIN_SIZE)/len(YEARS))*i, CANVAS_HEIGHT,
                           fill='black', width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX*i, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # for name_xx, year_dict in name_data.items():
    #     for year_xx in YEARS:
    #         if str(year_xx) not in year_dict:
    #             year_dict[year_xx] = 1000
    # 解決年份不存在的問題

    name_index = 0
    for name in lookup_names:
        for i in range(len(YEARS)):
            color = COLORS[name_index % len(COLORS)]
            if i+1 > 11:  # i + 1 out of range (next year doesn't exist)  # add name only
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX * i, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2,
                                   text= name + ' *', fill= color, anchor=tkinter.NW)
            else:  # within data range
                if str(YEARS[i]) not in name_data[name]:  # no record for the year
                    name_data[name][str(YEARS[i])] = 1000
                    if [str(YEARS[i + 1])] not in name_data[name]:  # no record for next year
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX * i, rank1,
                                           get_x_coordinate(CANVAS_WIDTH, i + 1) + TEXT_DX * (i + 1), 1000,
                                           fill=color, width=LINE_WIDTH)
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX * i, rank1,
                                           text=name + ' *', fill=color, anchor=tkinter.NW)
                    else:  # has record for next year
                        rank2 = name_data[name][str(YEARS[i + 1])]
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX * i, 1000,
                                           get_x_coordinate(CANVAS_WIDTH, i + 1) + TEXT_DX * (i + 1), rank2,
                                           fill=color, width=LINE_WIDTH)
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX * i, rank2,
                                           text=name + ' *', fill=color, anchor=tkinter.NW)
                else:  # has record for the year
                    if str(YEARS[i]) in name_data[name]:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX * i, name_data[name][str(YEARS[i])],
                                           get_x_coordinate(CANVAS_WIDTH, i + 1) + TEXT_DX * (i + 1),
                                           name_data[name][str(YEARS[i + 1])],
                                           fill=color, width=LINE_WIDTH)
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX * i, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2,
                                           text=lookup_names[name_index] + name_data[name][str(YEARS[i])], fill=color, anchor=tkinter.NW)
        name_index += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
