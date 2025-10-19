from bs4 import BeautifulSoup

def parser(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the main div with class "trail-grid"
    trail_grid = soup.find("div", class_="_44acb0dc _37345ed1 e32929ae bd361404 _868cc137 _9ebc6d94 _68f868a4")

    # Extract grid dimensions
    style_content = trail_grid.get("style").strip().split()
    n = int(style_content[-1][:-1])

    # Initialize an empty grid based on the extracted size
    grid = [[] for _ in range(n)]

    # Find all divs with class "trail-cell" inside the grid
    trail_cells = soup.find_all("div", attrs={"data-cell-idx": True})

    for cell in trail_cells:
        # Read the data-cell-idx attribute (position of the cell)
        cell_idx = int(cell.get("data-cell-idx"))
        
        # Check if there's a child div with class "trail-cell-content"
        content_div = cell.find("div", attrs={"data-cell-content": True})
        
        # Extract its text content if it exists
        content = int(content_div.get_text(strip=True)) if content_div else None

        # Append the content to the corresponding row based on cell index
        grid[cell_idx // n].append(content)
    
    return grid