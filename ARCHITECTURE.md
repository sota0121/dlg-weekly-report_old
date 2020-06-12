# System architecture

Name: Support to make DLG weekly report. (drep)

## Weekly report summary

- start date
  - <font color=yellow>input parameter</font>
- end date
  - <font color=yellow>input parameter</font>
- pick up topic threads
  - remarkable threads context and link
    - <font color=blue>extract threads which has the most replies</font>
- carried out events (meeting, meetup)
  - <font color=orange>manual</font>
- ranking
  - users who posted the most comments on this week
    - <font color=blue>extract users who posted the most comments</font>
  - channels which have the most comments on this week
    - <font color=blue>extract channels which have the most comments</font>
- coming soon events
  - <font color=orange>manual</font>
- others

## Input / Output

### Input

- start date
- end date

```bash
$ drep --start YYYY-MM-DD --end YYYY-MM-DD
```

### Output

- topic threads to pick up
- users who posted the most comments on this week
- channels which have the most comments on this week

```json
{
  "topic_threads_to_pick_up": [
    {
      "num_of_replies": 23,
      "num_of_reactions": 34,
      "link": "https://data-learning-guild.slack.com/archives/xxxxxxxxxxx"
    },
    {
      "num_of_replies": 18,
      "num_of_reactions": 20,
      "link": "https://data-learning-guild.slack.com/archives/xxxxxxxxxxx"
    },
    {
      "num_of_replies": 10,
      "num_of_reactions": 19,
      "link": "https://data-learning-guild.slack.com/archives/xxxxxxxxxxx"
    }
  ],
  "users_posted_the_most_comments": [
    {
      "user_name": "USER_NAME",
      "user_link": "https://data-learning-guild.slack.com/team/xxxxxx",
      "num_of_comments": 53
    },
    {
      "user_name": "USER_NAME",
      "user_link": "https://data-learning-guild.slack.com/team/xxxxxx",
      "num_of_comments": 42
    },
    :
  ],
  "channels_have_the_most_comments": [
    {
      "channel_name": "CHANNEL_NAME",
      "channel_link": "https://data-learning-guild.slack.com/archives/xxxxxxxx",
      "num_of_comments": 89
    },
    {
      "channel_name": "CHANNEL_NAME",
      "channel_link": "https://data-learning-guild.slack.com/archives/xxxxxxxx",
      "num_of_comments": 23
    },
    :
  ]
}
```
