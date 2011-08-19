# Copyright (C) 2007,2010,2011	Valek Filippov (frob@df.ru)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 3 or later of the GNU General Public
# License as published by the Free Software Foundation.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA
#

import sys,struct
import tree, gtk, gobject
import ole

def parse (cmd, entry, page):
	if cmd[0] == "$":
		pos = cmd.find("@")
		if pos != -1:
			chtype = cmd[1:pos]
			chaddr = cmd[pos+1:]
			print "Command: ",chtype,chaddr
		else:
			chtype = cmd[1:4]
			chaddr = "0"
		
		if "ole" == chtype.lower():
			treeSelection = page.view.get_selection()
			model, iter1 = treeSelection.get_selected()
			if iter1 == None:
				page.view.set_cursor_on_cell(0)
				treeSelection = page.view.get_selection()
				model, iter1 = treeSelection.get_selected()
			buf = model.get_value(iter1,3)
			if buf[int(chaddr,16):int(chaddr,16)+8] == "\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1":
				ole.parse (buf[int(chaddr,16):],page)
			else:
				print "OLE stream not found at ",chaddr