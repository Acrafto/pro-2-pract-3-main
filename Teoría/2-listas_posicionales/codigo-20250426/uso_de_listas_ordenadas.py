# -*- coding: utf-8 -*-

# Copyright 2019, Profesorado de Fundamentos de Programación II
#                 Grado en Ciencia e INgeneiría de Datos
#                 Facultade de Informática
#                 Universidade da Coruña
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from array_ordered_positional_list import ArrayOrderedPositionalList as OrderedPositionalList
#from linked_ordered_positional_list import LinkedOrderedPositionalList as OrderedPositionalList

def print_list(opl):
    """ Show a positional list in a terminal. """
    print("[", end=" ")
    for x in opl:
        print(x, end=" ")
    print("]")
        

        
def _print_test(mensaje, resultado):
    """ helper function to show the result of a test."""
    print(mensaje, end=": ")
    print(resultado, end=" ")
              
if __name__ == '__main__':
    # Ejemplos de utilización. NO es un test exhaustivo
    l = OrderedPositionalList(); print_list(l)
    _print_test("añadir 20", (l.add(20))); print_list(l)
    _print_test("añadir 30", (l.add(30))); print_list(l)
    _print_test("añadir 10", (l.add(10))); print_list(l)
    _print_test("añadir 40", (l.add(40))); print_list(l)
    _print_test("añadir 40", (l.add(40))); print_list(l)
    _print_test("añadir 10", (l.add(10))); print_list(l)
    _print_test("añadir 30", (l.add(30))); print_list(l)
    _print_test("añadir 25", (l.add(25))); print_list(l)
    _print_test("reemplazar 10", (l.replace(l.first(), 15))); print_list(l)
    
    