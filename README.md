# A Reddit Date Filter URL Generator

While browsing http://redditmetrics.com/, you might wonder, "what is responsible
for the spike in subscribers on a particular date?". This simple Python script
can help illustrate the answer by rendering the top-ranked posts in the subreddit
of your choice for a particular date.

It also works without a subreddit filter, but I'm not sure how valuable that
information is.

A simple date filter for viewing "what happened on date X" on Reddit.

## Installation (bash shell)

    git clone [project path]
    cd reddit-date-filter/
    pip install -r requirements.txt

## Execution

    python reddit_date_filter.py --help

## Example

    # Shows /r/pics submissions on January 1, 2015
    python reddit_date_filter.py -s pics 2015-01-01

