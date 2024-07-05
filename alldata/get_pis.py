from bs4 import BeautifulSoup

def get_pi_names(nct):
    # Correctly format the file path using f-string
    file_path = fr"C:\Users\prerk\OneDrive\Desktop\Prerana\Projects\IISER\CT-KnowledgeGraph\alldata\{nct}.html"
    
    # Read the HTML file
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <div> elements with the class name 'contact-funding-title'
    div_elements = soup.find_all('div', class_='contact-funding-title')

    # Check if any <div> elements were found
    if div_elements:
        # Get the last <div> element with the class 'contact-funding-title'
        last_div = div_elements[-1]
        
        # Find the <div> immediately following the last 'contact-funding-title' <div>
        next_div = last_div.find_next_sibling('div')
        
        # Print the last 'contact-funding-title' <div> and the following <div>, if found
        if next_div:
            extracted_text = next_div.get_text(separator=' ', strip=True)
            print(extracted_text)
            return extracted_text
    else:
        print("No <div> element with class 'contact-funding-title' found.")
        return None

# get_pi_names('NCT03003143')
