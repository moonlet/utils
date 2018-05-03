#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


def retry(max_retry_times, waiting_sec=1):
    """make the function with retry function

    Args:
        max_retry_times: the maximum retry times. -1 means infinite.
        waiting_sec: waiting seconds before every retry. default is 1 second.

    Examples:

        @retry(max_retry_times=3, waiting_sec=1)
        def request(url):
            print 'do some requesting things'
            raise ValueError('500')
    """

    def _decorator(func):

        def _func_params(*args, **kwargs):
            retry_index = 0
            while retry_index != max_retry_times:
                try:
                    return func(*args, **kwargs)
                except:
                    if waiting_sec > 0:
                        time.sleep(waiting_sec)
                    continue
                finally:
                    retry_index += 1

            raise RuntimeError('retried {} times'.format(max_retry_times))

        return _func_params

    return _decorator


if __name__ == '__main__':

    @retry(retry_times=3, waiting_sec=1)
    def request(url):
        print 'do some requesting things'
        raise ValueError('500')

    request('http://www.baidu.com')
