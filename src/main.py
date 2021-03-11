import click
from click import Abort
from scrapy.crawler import CrawlerProcess

from scraper.virtual_account import BCAScrapy, BNIScrapy, BRIScrapy, PermataScrapy, MandiriScrapy


@click.group()
def cli():
    pass


@click.command()
@click.argument('name')
@click.argument('va_number')
@click.argument('biller_code', required=False)
def va(name, va_number, biller_code=None):
    process = CrawlerProcess()

    if name == 'bca':
        process.crawl(BCAScrapy, va_number=va_number)

    if name == 'bri':
        process.crawl(BRIScrapy, va_number=va_number)

    if name == 'bni':
        process.crawl(BNIScrapy, va_number=va_number)

    if name == 'permata':
        process.crawl(PermataScrapy, va_number=va_number)

    if name == 'mandiri':
        biller_code = biller_code if biller_code else click.prompt('Input Biller Code:')
        process.crawl(MandiriScrapy, va_number=va_number, biller_code=biller_code)

    process.start()


cli.add_command(va)


if __name__ == '__main__':
    cli()
