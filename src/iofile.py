#
#   Python 3.12.1
#

import os
import re
import time
import numpy
import asyncio
from typing import Callable, List, Tuple


class IoPathFile:
    """
    Estrutura de dados para lidar com multiplos arquivos I/O
    """
    def __init__(
        self,
        funcs: List[Callable] = [],
        arg: List[Tuple] = [()]
    ) -> None:
        """Monta pilha de funcoes e argumentos"""
        self.__STACK_FUNCTION_: List[Callable] = funcs
        self.__STACK_FUNCTION_ARGS_: List[Tuple] = arg
        self.__bool_func_: bool = bool(self.__STACK_FUNCTION_)
        self.__bool_func_arg: bool = bool(self.__STACK_FUNCTION_ARGS_[0])

    def get_bool(self) -> dict:
        """
        Retorna um `dict` com o estado boleano da pilha de funcao e argumento.
        
        Returns
        -------
        dict -> `{'func': bool, 'arg': bool}`
        """
        return {'func': self.__bool_func_, 'arg': self.__bool_func_arg}

    

if __name__ == '__main__':
    io_path_file = IoPathFile()
    print(io_path_file.get_bool())
