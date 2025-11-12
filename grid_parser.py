from bs4 import BeautifulSoup
from collections import defaultdict

def parser(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the main div with class "trail-grid"
    trail_grid = soup.find_all("div", dir="ltr")[-1]

    # Extract grid dimensions
    style_content = trail_grid.get("style").strip().split()
    n = int(style_content[-1][:-1])

    # Initialize an empty grid based on the extracted size
    grid = [[] for _ in range(n)]

    # Initialize an empty dictonary based on the extracted size
    barriers = defaultdict(lambda: None)

    # Find all divs with class "trail-cell" inside the grid
    trail_cells = soup.find_all("div", attrs={"data-cell-idx": True})

    for cell in trail_cells:
        print(cell)
        # Read the data-cell-idx attribute (position of the cell)
        cell_idx = int(cell.get("data-cell-idx"))
        
        # Check if there's a child div with class "trail-cell-content"
        content_div = cell.find("div", attrs={"data-cell-content": True})
        
        # Extract its text content if it exists
        content = int(content_div.get_text(strip=True)) if content_div else None

        # Append the content to the corresponding row based on cell index
        grid[cell_idx // n].append(content)

        # Estract right barrier
        left_barrier = cell.find("div", class_="_9649408d")
        if left_barrier:
            barriers[((cell_idx // n, cell_idx % n),(cell_idx // n, (cell_idx % n) - 1))]
            barriers[((cell_idx // n, (cell_idx % n) - 1),(cell_idx // n, cell_idx % n))]

        # Estract left barrier
        right_barrier = cell.find("div", class_="_06db022a")
        if right_barrier:
            barriers[((cell_idx // n, cell_idx % n),(cell_idx // n, (cell_idx % n) + 1))]
            barriers[((cell_idx // n, (cell_idx % n) + 1),(cell_idx // n, cell_idx % n))]

        # Estract below barrier
        below_barrier = cell.find("div", class_=["_4dc74db0", "dc10fb47", "f87e98ef", "_99f642fd"])
        if below_barrier:
            print("ok")
            barriers[((cell_idx // n, cell_idx % n),((cell_idx // n) + 1, cell_idx % n))]
            barriers[(((cell_idx // n) + 1, cell_idx % n),(cell_idx // n, cell_idx % n))]
    
    return grid, barriers

# nuova strategia:
# 1) escludo i div figli con attributo data-cell-content