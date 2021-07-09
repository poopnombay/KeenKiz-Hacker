
# Get list of lenghts and list of widths
lengths = [1, 2, 3, 4, 5]
widths = [1, 2, 3, 4, 5]

# Verify length of the list of lengths and the length of the list of widths are the same
if len(lengths) == len(widths):
    # Get list of areas by multiplying list of lenghts and list of widths
    areas = []
    for i in range (0, len(lengths)):
        area = lengths[i] * widths[i]
        areas.append(area)
    print(areas[i])
else:
    print("Make sure lists of lengths and widths are the same")
