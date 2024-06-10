import os
from tkinter import filedialog
import subprocess
import ezdxf
import svgwrite
from svgwrite import cm, mm


def convert_dwg_to_dxf(dwg_file_path):
    # Define the output DXF file path
    dxf_file_path = dwg_file_path.replace(".dwg", ".dxf")

    # Command to convert DWG to DXF using TeighaFileConverter
    command = f'"C:/Program Files/ODA/Teigha File Converter/TeighaFileConverter.exe" "{dwg_file_path}" "{os.path.dirname(dwg_file_path)}" ACAD2010 DXF 1'
    subprocess.run(command, shell=True, check=True)

    return dxf_file_path


def dwg_to_svg(dwg_file_path, svg_file_path):
    # Convert DWG to DXF
    dxf_file_path = convert_dwg_to_dxf(dwg_file_path)

    # Load the DXF file
    doc = ezdxf.readfile(dxf_file_path)

    # Create a new SVG file
    dwg = svgwrite.Drawing(svg_file_path, profile="tiny")

    # Iterate over the entities in the DXF file
    for entity in doc.modelspace().query("LINE"):
        start = entity.dxf.start
        end = entity.dxf.end
        dwg.add(
            dwg.line(
                start=(start[0] * mm, start[1] * mm),
                end=(end[0] * mm, end[1] * mm),
                stroke=svgwrite.rgb(10, 10, 16, "%"),
            )
        )

    # Save the SVG file
    dwg.save()


# Example usage
dwg_file = filedialog.askopenfilename(
    title="Select DWG file", filetypes=[("DWG files", "*.dwg")]
)
svg_save = filedialog.asksaveasfilename(
    defaultextension=".svg", filetypes=[("SVG files", "*.svg")]
)
dwg_to_svg(dwg_file, svg_save)
