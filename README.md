# README
 History.db
 
# Notes
History.db contains the browsing history of a user. The database is in sqlite3 format. The database contains the following tables:
- history_client_versions: contains the version of the browser used by the user
- history_event_listeners: ? 
- history_events: ?  
- history_visits: contains the browsing history of the user; probably the most relevant.  Will have more rows than history_items.
- history_items: information about each individual web page visited by the user (one row per distinct website), including the following columns:
  - id: A unique identifier for each item.
  - url: The URL of the web page.
- history_items_to_tags: ?
- history_tags: ? 
- history_tombstones: 
- history_downloads: ? 
- metadata: ? 
- sqlite_sequence: ? 
- 

# resources

https://github.com/mgierschdev/browsingHistory
[Schema](https://gist.github.com/l1x/68e206f56bcc22cde3d76cc8fed49f3f)
[Sample jupyter notebook](https://notebook.community/mmathioudakis/web_browsing/browsing_history)
