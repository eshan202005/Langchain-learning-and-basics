from langchain_community.document_loaders import WebBaseLoader
url="https://www.flipkart.com/aquench-lean-stainless-steel-1l-water-bottle-combo-fridge-office-gym-home-use-1000-ml/p/itmd249787277019?pid=BOTHKPYKKN9GFPGR&lid=LSTBOTHKPYKKN9GFPGROWRRIS&marketplace=FLIPKART&store=upp%2F3t7&srno=b_1_1&otracker=browse&fm=organic&iid=en_xywhbD8mIEVn5rnBP5-HGY3b4GLRpvgrIXdwzOnbzL9wqCEFUiv3700ETbr7DYi6603GR73DwfxvJiBDbD-ZJA%3D%3D&ppt=None&ppn=None&ssid=61ydwue23k0000001779872441833&ov_redirect=true&ov_redirect=true"
loader = WebBaseLoader(url)

docs=loader.load()

print(docs[0].page_content)
