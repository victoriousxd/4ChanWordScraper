# 4ChanWordScraper
Scrape posts on 4 chan for popular words to get hip with young kid culture


# Goals
1. collect concrete list of boards into database
2. Create concrete classes to represent attributes of boards, posts, and threads

Once pages are succesfully scraped into classes then we can start formatting into database

We only want to store words and their word count for each day.


Database

Boards database with attributes
i.e. {
	"boards": [{
		"board": "a",
		"title": "Anime \u0026 Manga",
		"ws_board": 1,
		"per_page": 15,
		"pages": 10,
		"max_filesize": 4194304,
		"max_webm_filesize": 3145728,
		"max_comment_chars": 2000,
		"max_webm_duration": 120,
		"bump_limit": 500,
		"image_limit": 300,
		"cooldowns": {
			"threads": 600,
			"replies": 60,
			"images": 60
		},
		"meta_description": "\u0026quot;\/a\/ - Anime \u0026amp; Manga\u0026quot; is 4chan's imageboard dedicated to the discussion of Japanese animation and manga.",
		"spoilers": 1,
		"custom_spoilers": 1,
		"is_archived": 1
	},


Separate table for each board

Word | [date->count, date->count]
