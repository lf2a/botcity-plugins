from botcity.plugins.crawler import BotCrawlerPlugin

crawler = BotCrawlerPlugin(javascript_enabled=True)

url = "https://crawler-test.com/"

# Make the request
html = crawler.request(url)

# Get element by id
print(html.get_element_by_id('header_bg').value())  # Crawler Test two point oh!

# Get attribute value of element found above
print(html.get_attribute(attribute='id'))  # header_bg

# HTML body
print(html.value())

# HTML body
print(crawler.request_as_string(url))

# Get the first element found by tag name (selectors)
print(html.query_selector(selectors='span').value())  # two point oh!

# Making a new search to find all elements by tag (selectors) name and get by index
element = html.query_selector_all(selectors='a', index=2, reset=True)
print(element.value())  # Separate Desktop page with AMP page as AMP and Mobile

# Making a new search to find all elements by tag name (selectors). (returns generator)
elements = html.query_selector_iter_all(selectors='a', reset=True)
for ele in elements:
    print(ele.value())

# Making the new search to get num of elements by tag name (selectors)
total_elements = html.query_selector_all_size(selectors='a', reset=True)
print(total_elements)

# javascript test (wait_time=milliseconds)
# Making a request and waiting 2 seconds to finish the javascript HTTP request execution.
html = crawler.request(url='https://crawler-test.com/javascript/ajax-return-data', wait_time=2000)

# Making a new search to find all elements by tag name (selectors). (returns generator)
request_elements = html.query_selector_iter_all(selectors='p', reset=True)
for ele in request_elements:
    print(ele.value())
