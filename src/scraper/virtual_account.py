import scrapy
from scrapy import FormRequest


class BCAScrapy(scrapy.Spider):
    name = 'va_bca'
    start_urls = [
        'https://simulator.sandbox.midtrans.com/bca/va/index'
    ]
    success_message = 'Success Pay'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.va_number = kwargs.get('va_number')

    def parse(self, response, **kwargs):
        try:
            yield FormRequest.from_response(
                response,
                formdata={
                    'va_number': self.va_number
                },
                callback=self.after_submit_number
            )
        except ValueError:
            return

    def after_submit_number(self, response):
        try:
            yield FormRequest.from_response(
                response,
                callback=self.after_submit_pay
            )
        except ValueError:
            return

    def after_submit_pay(self, response):
        return {
            'status': self.success_message,
        }


class BRIScrapy(scrapy.Spider):
    name = 'va_bri'

    start_urls = [
        # 'https://simulator.sandbox.midtrans.com/bri/va/index'
        'https://stackoverflow.com/questions/55436331/notification-in-python-without-stopping-the-script',
    ]
    success_message = 'Success Pay'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.va_number = kwargs.get('va_number')

    def parse(self, response, **kwargs):
        try:
            yield FormRequest.from_response(
                response,
                formdata={
                    'va_number': self.va_number
                },
                callback=self.after_submit_number
            )
        except ValueError:
            return

    def after_submit_number(self, response):
        try:
            yield FormRequest.from_response(
                response,
                callback=self.after_submit_pay
            )
        except ValueError:
            return

    def after_submit_pay(self, response):
        return {
            'status': self.success_message,
        }


class BNIScrapy(scrapy.Spider):
    name = 'va_bni'
    start_urls = [
        'https://simulator.sandbox.midtrans.com/bni/va/index'
    ]
    success_message = 'Success Pay'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.va_number = kwargs.get('va_number')

    def parse(self, response, **kwargs):
        yield FormRequest.from_response(
            response,
            formdata={
                'va_number': self.va_number
            },
            callback=self.after_submit_number
        )

    def after_submit_number(self, response):
        try:
            yield FormRequest.from_response(
                response,
                callback=self.after_submit_pay
            )
        except ValueError:
            return

    def after_submit_pay(self, response):
        return {
            'status': self.success_message,
        }


class PermataScrapy(scrapy.Spider):
    name = 'va_permata'

    start_urls = [
        'https://simulator.sandbox.midtrans.com/permata/va/index'
    ]
    success_message = 'Success Pay'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.va_number = kwargs.get('va_number')

    def parse(self, response, **kwargs):
        yield FormRequest.from_response(
            response,
            formdata={
                'va_number': self.va_number
            },
            callback=self.after_submit_number
        )

    def after_submit_number(self, response):
        try:
            yield FormRequest.from_response(
                response,
                callback=self.after_submit_pay
            )
        except ValueError:
            return

    def after_submit_pay(self, response):
        return {
            'status': self.success_message,
        }


class MandiriScrapy(scrapy.Spider):
    name = 'va_mandiri'

    start_urls = [
        'https://simulator.sandbox.midtrans.com/mandiri/bill/index'
    ]
    success_message = 'Success Pay'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.biller_code = kwargs.get('biller_code')
        self.va_number = kwargs.get('va_number')

    def parse(self, response, **kwargs):
        yield FormRequest.from_response(
            response,
            formdata={
                'biller_code': self.biller_code,
                'bill_key': self.va_number,
            },
            callback=self.after_submit_number
        )

    def after_submit_number(self, response):
        try:
            yield FormRequest.from_response(
                response,
                callback=self.after_submit_pay
            )
        except ValueError:
            return

    def after_submit_pay(self, response):
        return {
            'status': self.success_message,
        }
