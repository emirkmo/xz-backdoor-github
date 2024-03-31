#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import date, datetime

import sys
import os

def plot(fname):
    df = pd.read_csv(fname)[1:]
    df['datetime'] = df['created_at'].map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))

    df['date'] = df['datetime'].map(lambda x: x.date())
    df['time'] = df['datetime'].map(lambda x: x.hour*60*60 + x.minute*60 + x.second)

    fig, ax = plt.subplots(1, figsize=(20,6))

    event_types = ['PushEvent', 'IssueCommentEvent', 'CreateEvent', 'DeleteEvent',
                   'PullRequestReviewCommentEvent', 'PullRequestReviewEvent',
                   'IssuesEvent', 'PullRequestEvent', 'CommitCommentEvent',
                   'ForkEvent', 'WatchEvent']

    for ev in event_types:
        filtered = df[df['event_type'] == ev]

        ax.scatter(filtered['date'], filtered['time'], s=4, label=ev, marker='o')

    step=2

    ax.legend(loc='lower left', fontsize='x-small')
    ax.set_title(fname)

    yticks = np.arange(0, 60*60*(24+step), 60*60*step)
    ylabels = [str(n).zfill(2) + ':00' for n in np.arange(0, 24+step, step)]
    ax.set_yticks(yticks)
    ax.set_yticklabels(ylabels)

    ax.set_xlim([date(2022, 2, 1), date(2024, 4, 1)])

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_minor_locator(mdates.DayLocator())

    ax.set_axisbelow(True)
    #ax.grid(visible=True, which='both')

    fig.tight_layout()

    os.makedirs("out", exist_ok=True)

    pdf_name = "out/" + os.path.splitext(fname)[0]+'.pdf'
    print(f'Writing {pdf_name}')
    fig.savefig(pdf_name)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} CSV")

    plot(sys.argv[1])
