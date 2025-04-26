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

from array_positional_list import ArrayPositionalList  as PositionalList
#from linked_positional_list import LinkedPositionalList as PositionalList

def print_list(pl):
    """ Show a positional list in a terminal. """
    print("[", end=" ")
    for x in pl:
        print(x, end=" ")
    print("]")
        
def print_list_reversed(pl):
    """ Show a positional list, in reverse order, in a terminal."""
    print("[", end=" ")
    marker = pl.last()
    while marker != None:
        print(pl.get_element(marker), end=" ")
        marker = pl.before(marker)
    print("]")
   
def insertion_sort(pl):
  """Sort PositionalList of comparable elements into nondecreasing order.
     WARNING: this is an UNSAFE function. 
              It only works with current implementations!
              This function ignores the postcondition of add_before 
              (invalidation of positions after the insertion position)"""
  if len(pl) > 1:                    # otherwise, no need to sort it
      marker = pl.first()
      while marker != pl.last():
          pivot = pl.after(marker)       # next item to place
          value = pl.get_element(pivot)
          if value > pl.get_element(marker):  # pivot is already sorted
              marker = pivot              # pivot becomes new marker
          else:                         # must relocate pivot
              walk = marker               # find leftmost item greater than value
              while walk != pl.first() and pl.get_element(pl.before(walk)) > value:
                  walk = pl.before(walk)
              pl.delete(pivot)
              pl.add_before(walk, value)   # reinsert value before walk
              

        
def search_element(pl, e):
    """ Return the position of the first instance of e in a positional list pl.
        Return None if e is not an element of pl."""
    marker = pl.first()
    while marker != None and pl.get_element(marker) != e:
        marker = pl.after(marker)
    return marker
    
def delete_list(pl):
    """ Delete all elements of positional list. """
    marker = pl.last()
    while marker != None:
        temp = pl.before(marker)
        pl.delete(marker)
        marker = temp
        
def copy_list(pl):
    """ Returns a copy of a positional list."""
    result = PositionalList()
    for x in pl:
        result.add_last(x)
    return result

def are_equal_lists(pl1, pl2):
    """ Return True if both positionl lists contains the same elements in the same order."""
    marker1 = pl1.first()
    marker2 = pl2.first()
    while marker1 != None and marker2 != None and \
          pl1.get_element(marker1) == pl2.get_element(marker2):
        marker1 = pl1.after(marker1)
        marker2 = pl2.after(marker2)
    return marker1 ==  marker2 == None
    
def delete_ocurrencies(pl, e):
    """ Delete all ocurrencies of element e in the positional list.
        Return the number fo courrences deleted."""
    marker = pl.first()
    prev = None
    count = 0
    while marker != None:
        if pl.get_element(marker) == e:
            pl.delete(marker)
            count += 1
            if prev == None:
                marker = pl.first()
            else:
                marker = pl.after(prev)
        else:
            prev = marker
            marker = pl.after(marker)
    return count

def delete_duplicates(pl):
    """ Remains only the first ocurrence of each element in a positional list."""
    marker1 = pl.first()
    prev2 = marker1
    marker2 = pl.after(marker1)
    count = 0
    while marker1 != None:
        while marker2 != None:
            if pl.get_element(marker1) == pl.get_element(marker2):
                pl.delete(marker2)
                count += 1
                marker2 = pl.after(prev2)
            else:
                prev2 = marker2
                marker2 = pl.after(marker2)
        marker1 = pl.after(marker1)
        if marker1 != None:
            prev2 = marker1
            marker2 = pl.after(marker1)
    return count

def concatenate(pl1, pl2):
    """Append the elementos of the second positional list to the end of the first list."""
    for x in pl2:
        pl1.add_last(x)
        
def _print_test(mensaje, resultado):
    """ helper function to show the result of a test."""
    print(mensaje, end=": ")
    print(resultado, end=" ")
              
if __name__ == '__main__':
    # Ejemplos de utilización. NO es un test exhaustivo
    l = PositionalList(); print_list(l)
    _print_test("añadir 20 al principio", (l.add_first(20))); print_list(l)
    _print_test("añadir 30 al final", (l.add_last(30))); print_list(l)
    _print_test("añadir 10 al principio", (l.add_first(10))); print_list(l)
    _print_test("añadir 40 al final", (l.add_last(40))); print_list(l)
    _print_test("añadir 15 antes del segundo", (l.add_before(l.after(l.first()), 15))); print_list(l)
    _print_test("añadir 25 antes del cuarto", (l.add_before(l.after(l.after(l.after(l.first()))), 25))); print_list(l)
    _print_test("añadir 17 después del segundo", (l.add_after(l.after(l.first()), 17))); print_list(l)
    _print_test("añadir 27 después del cuarto", (l.add_after(l.after(l.after(l.after(l.first()))), 27))); print_list(l)
    _print_test("mostrar el quinto", l.get_element(l.after(l.after(l.after(l.after(l.first())))))); print_list(l)
    _print_test("cambiar el quinto por 28", (l.replace(l.before(l.before(l.before(l.last()))), 28))); print_list(l)
    _print_test("mostrar el nuevo quinto", l.get_element(l.after(l.after(l.after(l.after(l.first())))))); print_list(l)
    _print_test("borrar el quinto", (l.delete(l.after(l.after(l.after(l.after(l.first()))))))); print_list(l)
    
    _print_test("ordenar", insertion_sort(l)); print_list(l)
    
    print("lista al revés", end=":" ); print_list_reversed(l) 
        
    _print_test("buscar el 25", search_element(l, 25)); print()
    _print_test("buscar el 26", search_element(l, 53)); print()

    m = (copy_list(l))
    _print_test("copiar lista", list(m)); print()
    
    _print_test("borrar la lista", delete_list(l)); print_list(l)

    _print_test("ordenar la lista vacía", insertion_sort(l)); print_list(l)
    _print_test("añadir 20 al principio", (l.add_first(20))); print_list(l)
    
    _print_test("iguales? (no)", are_equal_lists(l, m) ); print()
    _print_test("iguales? (sí)", are_equal_lists(l, l) ); print()
    _print_test("iguales? (sí)", are_equal_lists(PositionalList(), PositionalList()) ); print()
    _print_test("iguales? (no)", are_equal_lists(m, PositionalList()) ); print()

    _print_test("añadir 10 al principio", (m.add_first(10))); print_list(m)
    _print_test("añadir 40 al final", (m.add_last(40))); print_list(m)
    _print_test("borra ocurrencias del 10 (no)", delete_ocurrencies(m, 10)); print_list(m)
    _print_test("borra ocurrencias del 40 (no)", delete_ocurrencies(m, 40)); print_list(m)
    
    _print_test("añadir 10 al principio", (m.add_first(10))); print_list(m)
    _print_test("añadir 10 al principio", (m.add_first(10))); print_list(m)
    _print_test("añadir 40 al final", (m.add_last(40))); print_list(m)
    _print_test("añadir 40 al final", (m.add_last(40))); print_list(m)
    _print_test("eliminar duplicados", delete_duplicates(m)); print_list(m)
    
    _print_test("concatenar", concatenate(m,l)); print_list(m)
    _print_test("ordenar", insertion_sort(m)); print_list(m)

    n = PositionalList()
    n.add_first(10)
    n.add_first(20)
    n.add_first(30)
    n.add_first(40)
    n.add_first(50)
    n.add_first(60)
    print_list(n)
    _print_test("ordenar", insertion_sort(n)); print_list(n)
    # errores
    #_print_test("añadir 100 en posición non válida", (l.add_before(7, 100)))
    #_print_test("añadir 100 en posición non válida", (l.add_after(7, 100)))
    #_print_test("borrar en posición non válida", (l.delete(7)))
    #_print_test("borrar en posición non válida", (l.replace(7, 100)))