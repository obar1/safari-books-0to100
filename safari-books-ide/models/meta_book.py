"""MetaBook:"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import re

from configs.config import ConfigMap


class MetaBook:
    """MetaBook."""
    epub_suffix = '.epub'
    HTTP_OREILLY = 'https://learning.oreilly.com/library/cover'
    GENERIC_HTTP_OREILLY = 'https://learning.oreilly.com/library/'

    def __init__(self, config_map: ConfigMap, persist_fs, process_fs, http_url: str):
        """init"""
        self.config_map = config_map
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.isbn = self.__get_isbn(http_url)
        self.contents_path = config_map.get_books_path + f'/{self.isbn}'
        self.dir_json = f"{self.contents_path}/{self.isbn}.json"
        self.dir_epub = f"{self.contents_path}/{self.isbn}.epub"
        self.dir_pdf = f"{self.contents_path}/{self.isbn}.pdf"
        self.dir_img = f"{self.contents_path}/{self.isbn}.png"

    def __repr__(self):
        """repr"""
        return f"MetaBook {self.http_url}, {self.isbn} {self.contents_path}"

    @classmethod
    def build_from_dir(cls, config_map, persist_fs, process_fs, dir_name):
        """build from dir"""
        return MetaBook(config_map, persist_fs, process_fs, http_url=cls.GENERIC_HTTP_OREILLY + '/' + dir_name)

    def get_img(self):
        """get img from the web"""
        self.process_fs.get_img(self.dir_img, f"{self.HTTP_OREILLY}/{self.isbn}/")

    def get_epub(self):
        """get epub from the web"""
        self.clean_ebooks()
        self.process_fs.get_epub(self.config_map, self.dir_epub, self.isbn)
        self.persist_fs.copy_file_to(self.get_epub_path(), self.dir_epub)

    @staticmethod
    def is_valid_ebook_path(ebook_folder):
        """check folder is 0123..9 like ISBN"""
        return re.match(r'[0-9]+', ebook_folder)

    def write(self):
        """write to fs"""
        # {
        #     "isbn": "0596007124",
        #     "http_url": "https://learning.oreilly.com/library/view/head-first-design/0596007124/"
        # }
        txt = []
        txt.append(
            f"""{{
"isbn": "{self.isbn}",
"http_url": "{self.http_url}"
        }}"""
        )
        self.persist_fs.make_dirs(self.contents_path)
        self.persist_fs.write_file(self.dir_json, txt)
        # self.persist_fs.create_file(self.dir_epub)
        self.get_epub()
        self.persist_fs.create_file(self.dir_pdf)
        # self.persist_fs.create_file(self.dir_img)
        self.get_img()

    def read_json(self):
        return self.persist_fs.read_file(self.dir_json)

    def __get_isbn(self, http_url):
        """get isbn
        it's the last 0123456..9
        """
        http_url = http_url.strip('/')
        return http_url[http_url.rfind('/') + 1:]

    def clean_ebooks(self):
        """del all the ebooks into the folder"""
        dirs = self.persist_fs.list_dirs(self.config_map.get_download_engine_books_path)
        valid_dirs = [dir_ for dir_ in dirs if MetaBook.is_valid_ebook_path(dir_)]
        for dir_ in valid_dirs:
            assert self.is_valid_ebook_path(dir_)
            self.persist_fs.delete_folder(dir_)

    def get_epub_path(self):
        """find the actual path into the path given the isbn
        dirs are supposed to be like
        download_engine_books_path/books title(isbn)
        """
        download_engine_books_path = self.config_map.get_download_engine_books_path
        isbn = self.isbn
        dirs = self.persist_fs.list_dirs(download_engine_books_path)
        dir_isbn = [dir_ for dir_ in dirs if '(' + isbn + ')' in dir_]
        assert len(dir_isbn) <= 1
        return download_engine_books_path + '/' + dir_isbn[0] + '/' + isbn + MetaBook.epub_suffix
