import matplotlib as mpl
import brewer2mpl
import matplotlib.ticker as tick
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True

# brewer2mpl.get_map args: set name  set type  number of colors
bmap = brewer2mpl.get_map('Dark2', 'qualitative', 6)
colors = bmap.mpl_colors

bmap2 = brewer2mpl.get_map('Paired', 'qualitative', 12)
colors2 = bmap2.mpl_colors

linestyles = [
     'solid',      # Same as (0, ()) or '-'
     'dashed',    # Same as '--'
     'dotted',    # Same as (0, (1, 1)) or '.'
     'dashdot',  # Same as '-.'
     (0, (3, 1, 1, 1)),
     (0, (1, 10)),
     (0, (1, 1)),
     (0, (1, 1)),
     (0, (5, 10)),
     (0, (5, 5)),
     (0, (5, 1)),
     (0, (3, 10, 1, 10)),
     (0, (3, 5, 1, 5)),
     (0, (3, 5, 1, 5, 1, 5)),
     (0, (3, 10, 1, 10, 1, 10)),
     (0, (3, 1, 1, 1, 1, 1))]

markers = ['*', '^', 'o', 'P', 'p', 'v']
markersizes = [15, 12, 12, 12, 12, 12]
patterns = [ "\\" , "/" , "|" , "+" , "-", ".", "*","x", "o", "O" ]

def fix_hist_step_vertical_line_at_end(ax):
    axpolygons = [poly for poly in ax.get_children() if isinstance(poly, mpl.patches.Polygon)]
    for poly in axpolygons:
        poly.set_xy(poly.get_xy()[:-1])

def y_fmt(tick_val, pos):
    if tick_val > 1000000000:
        val = tick_val/1000000000.0
        return "%.01fB" % (val)
    elif tick_val > 1000000:
        val = tick_val/1000000.0
        return "%.01fM" % (val)
    elif tick_val > 1000:
        val = tick_val/1000.0
        return "%.01fk" % (val)
    else:
        return tick_val

def y_fmt_b(tick_val, pos):
    val = tick_val/1000000000.0
    return "%.01fB" % (val) if val%1 else "%dB" % int(val)

def y_fmt_m(tick_val, pos):
    val = tick_val/1000000.0
    return "%.01fM" % (val) if val%1 else "%dM" % int(val)

def y_fmt_k(tick_val, pos):
    val = tick_val/1000.0
    return "%.01fK" % (val) if val%1 else "%dK" % int(val)

# unit for device 50k
dev_unit = 50000
# unit for counter 200M
cnt_unit = 150000000

def y_fmt_dev(tick_val, pos):
    global dev_unit
    val = tick_val/dev_unit
    return "%.01fX" % (val) if val%1 else "%dX" % int(val)

def y_fmt_cnt(tick_val, pos):
    global cnt_unit
    val = tick_val/cnt_unit
    return "%.01fX" % (val) if val%1 else "%dX" % int(val)