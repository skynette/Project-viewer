  var site_url                            = 'index.html',
        pagination_next_page_number         = '2',
        pagination_available_pages_number   = '2',
        pagination_loading_text             = 'Loading',
        pagination_more_posts_text          = 'More Posts',
        clipboard_copied_text               = 'Link copied to clipboard';

// Add current class the to current tag item if the URL matches the tag URL
				window.addEventListener("DOMContentLoaded", (event) => {
					var url_pathname = window.location.pathname;

					document
						.querySelectorAll(".c-tags-list__link")
						.forEach(function (index) {
							var current_tag_item = index;
							if (url_pathname === current_tag_item.getAttribute("href")) {
								current_tag_item.className +=
									" " + "c-tags-list__link--current";
							}
						});
				});
