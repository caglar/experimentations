from __future__ import division

from dataset import Dataset
import numpy as np

class Sphere:

	def __init__(self, Xs):
		self.center = np.mean(Xs)
		self.end_point, self.radius = self.find_end_point(Xs)	

	def find_end_point(self, Xs):
		end_point = Xs[0]
		max_d = np.linalg.norm(Xs[0]-self.center)

		for i in xrange(1, Xs.shape[0]):
			dist = np.linalg.norm(Xs[i] - self.center)
			if dist > max_d:
				end_point =	Xs[i]
				max_d = dist
		radius = np.linalg.norm(end_point-self.center)

		return end_point, radius
	
	def check_example_in_sphere(self, x):
		dist = np.linalg.norm(self.center-x)
		if dist <= self.radius:
			return True
		return False

class SphericalSimulation:

	def __init__(self, data_path=None):

		self.data_path = data_path
		ds = Dataset(is_binary=True)
		ds.setup_dataset(data_path=self.data_path, train_split_scale=0.6)

		self.X = ds.Xtrain
		self.y = ds.Ytrain

		self.y = np.cast['uint8'](list(self.y))
		self.X = np.cast['float32'](list(self.X))

	def get_data_classes(self, path):
		X1s = []
		X0s = []
		for i in xrange(self.y.shape[0]):
			if self.y[i] ==1:	
				X1s.append(self.X[i])
			else:
				X0s.append(self.X[i])
		return [np.array(X0s), np.array(X1s)]

	def fit_spheres_to_data(self, path):
		data_classes = self.get_data_classes(path)
		sphere1 = Sphere(data_classes[0])
		sphere2 = Sphere(data_classes[1])
		return [sphere1, sphere2]
	
	def is_point_in_both_spheres(self, x, spheres):
		if spheres[0].check_example_in_sphere(x) and spheres[1].check_example_in_sphere(x):
			return True
		return False

	def run_mc_sim(self, data_path=None, sim_size=2000):
		if data_path == None:
			data_path = self.data_path
		print "Started fitting spheres to the data"
		spheres = self.fit_spheres_to_data(data_path)

		print "Spheres are fitted to the data"
		example_ids = np.random.randint(self.X.shape[0], size=sim_size)
		no_of_trials = example_ids.shape[0]
		no_of_ints = 0
		print "MC simulation started"
		for i in example_ids:
			if self.is_point_in_both_spheres(self.X[i], spheres):
				no_of_ints +=1
		hit_rate = no_of_ints/float(no_of_trials)
		return (hit_rate)*100

if __name__=="__main__":
	data_path = "/home/caglar/Datasets/tetropentomino/pento64x64_simple_40k.npy"
	sim = SphericalSimulation(data_path)
	hit_rate = sim.run_mc_sim()
	print "Hit rate is %d" % (hit_rate)
