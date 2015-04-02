#!/bin/env python
# Loads posts made on a particular date. Useful for tracking down content 
# that may be responsible for generating a spike in subscribers from
# looking at sites such as http://redditmetrics.com/

import click
from datetime import datetime, timedelta
from urllib import urlencode
import webbrowser

@click.command()
@click.option("--subreddit", "-s", default=None, 
              help="Restrict results to subreddit (default: show all)")
@click.option("--delta", "-d", default=1, type=click.IntRange(1, 7, clamp=True), 
              help="Time delta in days (default: 1)")
@click.argument("date")
def openbrowser(subreddit, delta, date):
    date_parts = [int(x) for x in date.split('-')]
    if len(date_parts) != 3:
        raise click.BadParameter("Date must be in format YYYY-MM-DD", 
                                 param=date)
    date_start = datetime(*date_parts)
    date_end = date_start + timedelta(hours=int(delta * 24))
    url_prefix = "http://www.reddit.com"
    if subreddit:
        url_prefix += "/r/%s" % (subreddit,)
    url_query = {
        "sort": "top",
        "q": "timestamp:%s..%s" % (date_start.strftime("%s"), date_end.strftime("%s")),
        "syntax" : "cloudsearch",
    }
    if subreddit:
        url_query["restrict_sr"] = str(subreddit)
    url_full = "%s/search?%s" % (url_prefix, urlencode(url_query))

    # now what?
    #click.echo("URL: %s" % (url_full,))

    webbrowser.open(url_full)

if __name__ == "__main__":
    openbrowser()
