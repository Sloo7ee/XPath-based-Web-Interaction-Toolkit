## "XPath-based Web Interaction Toolkit

## idea : 

1. `XPATHc(path)`
   - This function is responsible for clicking on an element on a web page using its XPath.
   - It uses the `WebDriverWait` function to wait until the element becomes clickable.
   - The function takes a `path` parameter, which represents the XPath of the element to be clicked.
   - After the element becomes clickable, it is clicked, and then the function returns the clicked element.

2. `XPATHs(path, Keys)`
   - This function is used to send keys (e.g., text) to an input element on a web page using its XPath.
   - Similar to `XPATHc`, it uses `WebDriverWait` to wait until the element becomes clickable.
   - The function takes two parameters: `path`, which represents the XPath of the input element, and `Keys`, which is the value to be sent to the input element.
   - Once the element is clickable, the specified value is sent to the element, and then the function returns the element.

3. `XPATHd(path)`
   - This function is used to retrieve data from a web page using its XPath, such as text content.
   - Again, it uses `WebDriverWait` to wait until the element becomes clickable.
   - The function takes a `path` parameter, which represents the XPath of the desired element.
   - Once the element becomes clickable, it is returned by the function, allowing you to use the returned element in further operations.

In summary, these functions provide a more concise way to interact with web pages using XPath. By encapsulating the common actions of clicking, sending keys, and retrieving data, you can reuse these functions and simplify your code when interacting with web elements. The XPaths can be obtained by inspecting the elements on the web page, copying their XPath, and using them as input to these functions.

## How to get XPATH :

To extract XPath, follow these steps using the Chrome browser's inspection tool:

1. Open the webpage for which you want to extract the XPath in Google Chrome.

2. Right-click on the element you want to extract the XPath for. A context menu will appear.

3. Click on "Inspect" in the menu. The inspection tool will open at the bottom of the browser.

4. The inspection tool will highlight the HTML code corresponding to the selected element. Right-click on the highlighted code.

5. In the context menu, hover over "Copy" and then click on "Copy XPath". The XPath for the selected element will be copied to the clipboard.

You can now use the copied XPath in your code or wherever you need to reference that specific element on the webpage.
