#!/usr/bin/env python3
# Copyright (C) 2022 @doegox
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import *

class ClosedBoxBurnXY(Boxes):
    """Fully closed box"""

    ui_group = "Box"

    description = """This box is more of a building block than a finished item.
Use a vector graphics program (like Inkscape) to add holes or adjust the base
plate.
It supports different values for burn on X and Y axis"""

    def __init__(self):
        Boxes.__init__(self)

        self.addSettingsArgs(edges.FingerJointSettings)
        self.buildArgParser("x", "y", "h", "outside")
        self.argparser.add_argument(
            "--burnx",  action="store", type=float, default=None,
            help="burn value on X axis")
        self.argparser.add_argument(
            "--burny",  action="store", type=float, default=None,
            help="burn value on Y axis")

    def render(self):
        x, y, h = self.x, self.y, self.h
        if self.outside:
            x = self.adjustSize(x)
            y = self.adjustSize(y)
            h = self.adjustSize(h)
        t = self.thickness

        self.moveTo(t, t)

        # self.rectangularWall(x, h, "FFFF", move="right", label="Wall 1")
        # self.rectangularWall(y, h, "FfFf", move="up", label="Wall 2")
        # self.rectangularWall(y, h, "FfFf", label="Wall 4")
        # self.rectangularWall(x, h, "FFFF", move="left up", label="Wall 3")
        # self.rectangularWall(x, y, "ffff", move="right", label="Top")
        # self.rectangularWall(x, y, "ffff", label="Bottom")
        if self.burnx is not None:
            self.spacing += 2 * self.burnx
        else:
            self.spacing += 2 * self.burn
        if self.burny is not None:
            self.spacing += 2 * self.burny
        else:
            self.spacing += 2 * self.burn


        if self.burnx is not None:
            self.burn = self.burnx
        self.text("Wall 1", x/2, 0, align="center")
        self.edges["F"](x)
        self.polyline(t, 90, t)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["F"](h)
        self.polyline(t, 90, t)
        if self.burnx is not None:
            self.burn = self.burnx
        self.edges["F"](x)
        self.polyline(t, 90, t)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["F"](h)
        self.polyline(t, 90, t)

        self.moveTo(x+t+self.spacing+t, 0)

        if self.burnx is not None:
            self.burn = self.burnx
        self.text("Wall 2", y/2, 0, align="center")
        self.edges["F"](y)
        self.polyline(0, 90, t)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["f"](h)
        self.polyline(t, 90, 0)
        if self.burnx is not None:
            self.burn = self.burnx
        self.edges["F"](y)
        self.polyline(0, 90, t)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["f"](h)
        self.polyline(t, 90, 0)

        self.moveTo(0, t+h+t+self.spacing)

        if self.burnx is not None:
            self.burn = self.burnx
        self.text("Wall 4", y/2, 0, align="center")
        self.edges["F"](y)
        self.polyline(0, 90, t)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["f"](h)
        self.polyline(t, 90, 0)
        if self.burnx is not None:
            self.burn = self.burnx
        self.edges["F"](y)
        self.polyline(0, 90, t)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["f"](h)
        self.polyline(t, 90, 0)

        self.moveTo(-t-self.spacing-t-x, 0)

        if self.burnx is not None:
            self.burn = self.burnx
        self.text("Wall 3", x/2, 0, align="center")
        self.edges["F"](x)
        self.polyline(t, 90, t)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["F"](h)
        self.polyline(t, 90, t)
        if self.burnx is not None:
            self.burn = self.burnx
        self.edges["F"](x)
        self.polyline(t, 90, t)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["F"](h)
        self.polyline(t, 90, t)

        self.moveTo(0, t+h+t+self.spacing+t)

        if self.burnx is not None:
            self.burn = self.burnx
        self.text("Top", x/2, 0, align="center")
        self.edges["f"](x)
        self.polyline(0, 90, 0)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["f"](y)
        self.polyline(0, 90, 0)
        if self.burnx is not None:
            self.burn = self.burnx
        self.edges["f"](x)
        self.polyline(0, 90, 0)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["f"](y)
        self.polyline(0, 90, 0)

        self.moveTo(x+t+self.spacing+t, 0)

        if self.burnx is not None:
            self.burn = self.burnx
        self.text("Bottom", x/2, 0, align="center")
        self.edges["f"](x)
        self.polyline(0, 90, 0)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["f"](y)
        self.polyline(0, 90, 0)
        if self.burnx is not None:
            self.burn = self.burnx
        self.edges["f"](x)
        self.polyline(0, 90, 0)
        if self.burny is not None:
            self.burn = self.burny
        self.edges["f"](y)
        self.polyline(0, 90, 0)
