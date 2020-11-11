import requests
from tqdm import tqdm


class SubFinder:

	def __init__(self, domain, out = True):
		self.domain = domain
		self.dataset = "subdomains-10000.txt"
		self.subdomain_list = []
		self.out = out

	def _read(self):
		"""
		Reading subdomain dataset
		"""
		with open(self.dataset, "r+") as file:
			self.content = file.read()
			self.subdomains = self.content.splitlines()

	def _out(self):
		"""
		Out to report file.
		"""
		with open(f"report-of-{self.domain}.txt", "w") as file:
			for subdomain in self.subdomain_list:
				file.write(subdomain + "\n")

	def run(self):
		"""
		Running the script
		"""
		self._read()

		for sd in tqdm(self.subdomains):
			url = f"http://{sd}.{self.domain}"
			try:
				requests.get(url)

			except requests.ConnectionError:
				pass

			else:
				self.subdomain_list.append(url)
				print(f"\nFounded subdomain: {url}\n")

		if (self.out == True):
			self._out()


		print("\nFinished. Subdomains are:")
		for sub in self.subdomain_list:
			print(sub)


if __name__ == '__main__':
	
	sdom = input("Domain: ")
	x = SubFinder(sdom)
	x.run()
