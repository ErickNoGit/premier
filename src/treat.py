#
#   PYTHON 3.12.1
#
#

import os
import re
import pprint
from bs4 import BeautifulSoup   # type : ignore

class FileLoad:
    """
    Estrutura de dados que carrega documento(s) HTML(s).

    Atraves da leitura de arquivo(s) e diretorio(s), retorna dados primitivos.
    """

    def read_html(self, html_path: str) -> str:
        """
        Executa a leitura de um arquivo HTML e retorna o texto.

        Parameters
        ----------
        html_path : str
            Caminho completo do arquivo `*.html`

        Returns
        -------
        str :
            Texto completo do arquivo `*.html`
        """
        with open(html_path, 'r', encoding='utf-8') as file:    
            soup = BeautifulSoup(file.read(), 'html.parser')
            return soup.text.strip()

    def read_dir_html(self, dir_html: str) -> list[str]:
        """
        Le um diretorio com arquivos html e retorna uma lista com conteudo.

        Parameters
        ----------
        dir_html : str
            Local dos arquivos html -> `/caminho/diretorio/`

        Returns
        -------
        list[str] :
            Lista de string, sendo cada string o texto completo do html
        """
        absdir = str(os.path.abspath(dir_html))
        path_abs = [str(os.path.join(absdir, f)) for f in os.listdir(absdir)]
        return list(map(lambda t: f'{self.read_html(t)}', path_abs))


class Treat(FileLoad):
    """
    Estrutura de dados que trata string e dados primitivos com string.
    """
    def __init__(self) -> None:
        super().__init__()

    def clean_text(self, content: str | list[str]) -> list[str]:
        """
        Remove espacos adicionas da string ou lista de string.

        Parameters
        ----------
        content : str | list[str]
            Texto com multiplos espacos, ou lista de texto

        Returns
        -------
        list[str] :
            Lista de string com texto(s) formatado(s)
        """
        if isinstance(content, list):
            return list(map(lambda t: re.sub(r'\s+', ' ', t).strip(), content))
        else:
            return [re.sub(r'\s+', ' ', content).strip()]

    def next_text(self, txt: str, cut: str) -> str:
        """
        Remove a parte anterior da string e retorna o restante.

        Parameters
        ----------
        txt : str
            Texto que sera cortado
        cut : str
            Palavra reservada dentro do texto, e o alvo do corte

        Returns
        -------
        str :
            Texto cortado
        """
        index = txt.find(cut)
        return txt[index:].strip() if index != -1 else txt

    def previos_text(self, txt: str, limit: str) -> str:
        """
        Remove a parte da string e retorna o restante anterior.

        Parameters
        ----------
        txt : str
            Texto que sera cortado
        limit : str
            Palavra reservada dentro do texto, e o alvo do limite

        Returns
        -------
        str :
            Texto cortado ou texto inserido
        """
        index = txt.find(limit)
        return txt[:index + len(limit)].strip() if index != -1 else txt

    def get_part_text(
        self,
        iter: list[str] | tuple[str],
        init: str,
        end: str
    ) -> list[str]:
        """
        Recolhe e retorna uma parte do texto selecionado

        Parameters
        ----------
        iter : list[str] | tuple[str]
            Iterador com a(s) string(s) para selecao
        init : str
            String inicial da fatia (incluida no iterador)
        end : str
            String final da fatia (incluida no iterador)

        Returns
        -------
        list[str] :
            Lista com a(s) string(s) fatiadas
        """
        return [self.previos_text(self.next_text(s, init), end) for s in iter]

    def re_replace(
        self,
        iter: list[str] | tuple[str],
        pattern: str,
        sub: str
    ) -> list[str]:
        """
        Subistitui o padrao encontrado em cada string.

        Parameters
        ----------
        iter : list[str] | tuple[str]
            Iterador com a(s) string(s) para selecao
        pattern : str
            Padrao regex que deve ser selecionado
        sub : str
            String ou regex da modificacao

        Returns
        -------
        list[str] :
            Lista com a(s) string(s) modificada(s)
        """
        return [re.sub(pattern, sub, texto) for texto in iter]

    def modif(
        self,
        iter: str | list[str] | tuple[str],
        target: str,
        rplace: str
    ) -> list[str]:
        """
        Modifica uma string por outra, realiza uma troca
        
        Parameters
        ----------
        iter : str | list[str] | tuple[str]
            Iterador com a(s) string(s) para modificacao
        target : str
            Palavra chave, alvo de modificacao
        rplace : str
            Palavra de substituicao
        
        Returns
        -------
        list[str] :
            Lista com a(s) string(s) modificada(s)
        """
        if isinstance(iter, str):
            return [iter.replace(target, rplace)]
        else:
            return [s.replace(target, rplace) for s in iter]

    def revers(self, iter: str | list[str] | tuple[str]) -> list[str]:
        """
        Reverte uma string ou um objeto de iteracao com strings
        
        Parameters
        ----------
        iter : str | list[str] | tuple[str]
        
        Returns
        -------
        list[str] :
            Lista com a(s) string(s) invertidas, mas na mesma ordem de index
        """
        return [iter[::-1]] if isinstance(iter, str) else [s[::-1] for s in iter]

if __name__ == '__main__':
    load = FileLoad()
    treat = Treat()
