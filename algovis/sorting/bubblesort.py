"""
Author: Mayank Arora (hotshot07)
"""
from ._base_class import BaseClass
from ._timer import Timer
from ._animation import AnimateAlgorithm
import copy


class BubbleSort(BaseClass):

    def __init__(self, datalist):
        super().__init__(datalist)
        self.__datalist = datalist

    def __repr__(self):
        return f'algovis.sorting.bubblesort.BubbleSort({self.__datalist})'

    # A generator for the ascending bubble sort algorithm
    def __ascending_sort_algo(self):
        _asc_list = copy.deepcopy(self.__datalist)
        _length_of_list = len(_asc_list)
        _has_swapped = True
        _number_of_iterations = 0

        while _has_swapped:
            _has_swapped = False

            for i in range(_length_of_list - _number_of_iterations - 1):
                if _asc_list[i] > _asc_list[i + 1]:
                    _asc_list[i], _asc_list[i + 1] = _asc_list[i + 1], _asc_list[i]
                    _has_swapped = True

            _number_of_iterations += 1
            yield _asc_list

    # A generator for the descending bubble sort algorithm
    def __descending_sort_algo(self):
        _desc_list = copy.deepcopy(self.__datalist)
        _length_of_list = len(_desc_list)
        _has_swapped = True
        _number_of_iterations = 0

        while _has_swapped:
            _has_swapped = False

            for i in range(_length_of_list - _number_of_iterations - 1):
                if _desc_list[i] < _desc_list[i + 1]:
                    _desc_list[i], _desc_list[i + 1] = _desc_list[i + 1], _desc_list[i]

                    _has_swapped = True

            _number_of_iterations += 1
            yield _desc_list

    # The function that is called by sort method
    def __sort_it(self, reverse, steps):
        _iteration_dict = {}
        iterations = 0

        if not reverse:
            for _yielded_list in self.__ascending_sort_algo():
                iterations += 1
                _iteration_dict[iterations] = copy.deepcopy(_yielded_list)
        else:
            for _yielded_list in self.__descending_sort_algo():
                iterations += 1
                _iteration_dict[iterations] = copy.deepcopy(_yielded_list)

        if steps:
            print()
            print("Iteration    List")
            for _iter, _list in _iteration_dict.items():
                print("    " + str(_iter) + "        " + str(_list))

            print()
        return _iteration_dict

    # Evaluating time of ascending bubble sort
    # Didn't use generators as I dont wanna waste time in dealing
    # with overheads
    def __time_eval_asc(self, iterations):
        _time_list = copy.deepcopy(self.__datalist)
        _length_of_list = len(_time_list)
        _timing_list = []

        while iterations:
            _has_swapped = True
            _number_of_iterations = 0

            timer = Timer()
            timer.start()

            while _has_swapped:
                _has_swapped = False

                for i in range(_length_of_list - _number_of_iterations - 1):
                    if _time_list[i] > _time_list[i + 1]:
                        _time_list[i], _time_list[i + 1] = _time_list[i + 1], _time_list[i]

                        _has_swapped = True

                _number_of_iterations += 1

            stop = timer.stop()
            _timing_list.append(stop)
            iterations -= 1
            _time_list = copy.deepcopy(self.__datalist)

        return _timing_list

    # Evaluating time of descending bubble sort
    def __time_eval_desc(self, iterations):
        _time_list = copy.deepcopy(self.__datalist)
        _length_of_list = len(_time_list)
        _timing_list = []

        while iterations:
            _has_swapped = True
            _number_of_iterations = 0

            timer = Timer()
            timer.start()

            while _has_swapped:
                _has_swapped = False

                for i in range(_length_of_list - _number_of_iterations - 1):
                    if _time_list[i] < _time_list[i + 1]:
                        _time_list[i], _time_list[i + 1] = _time_list[i + 1], _time_list[i]

                        _has_swapped = True

                _number_of_iterations += 1

            stop = timer.stop()
            _timing_list.append(stop)
            iterations -= 1
            _time_list = copy.deepcopy(self.__datalist)

        return _timing_list

    def sort(self, reverse=False, steps=False):
        _sorted_object = self.__sort_it(reverse, steps)
        return list(_sorted_object.values())[-1]

    def evaluate(self, reverse=False, iterations=1):
        if reverse:
            _timing_list = self.__time_eval_desc(iterations)
        else:
            _timing_list = self.__time_eval_asc(iterations)

        _minimum_time = str("{:.10f}s".format(min(_timing_list)))
        _maximum_time = str("{:.10f}s".format(max(_timing_list)))
        _average_time = str("{:.10f}s".format(sum(_timing_list) / iterations))

        eval_dict = {
            "Minimum Time:": _minimum_time,
            "Maximum Time:": _maximum_time,
            "Average Time:": _average_time
        }
        return eval_dict

    def visualize(self, reverse=False, interval=250):
        _vis_list = copy.deepcopy(self.__datalist)

        if not reverse:
            AnimateAlgorithm("Bubble Sort", _vis_list, self.__ascending_sort_algo(), interval)
        else:
            AnimateAlgorithm("Bubble Sort", _vis_list, self.__descending_sort_algo(), interval)

    @classmethod
    def info(cls):
        information = """
           Bubble Sort

In Bubble Sort  we look at pairs of adjacent elements in an array,
one pair at a time, and swap their positions if the first element is
larger than the second, or simply move on if it isn't.

        ---Time Complexity---
        "Worse case: O(n^2)
        "Average case: O(n^2)
        "Best case: O(n)

        ---Space Complexity---
        O(n) total, O(1) auxiliary

        ---Algorithm---
        procedure bubbleSort(A : list of sortable items)
            n := length(A)
            repeat
                swapped := false
                    for i := 1 to n - 1 inclusive do
                        if A[i - 1] > A[i] then
                        swap(A[i - 1], A[i])
                        swapped = true
                        end if
                    end for
                    n := n - 1
                until not swapped
        end procedure"""

        return information
