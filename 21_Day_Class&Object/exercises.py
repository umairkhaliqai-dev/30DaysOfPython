ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        """Initialize with a list of data"""
        self.data = data
    
    def count(self):
        """Return the number of elements"""
        return len(self.data)
    
    def sum(self):
        """Return the sum of all elements"""
        return sum(self.data)
    
    def min(self):
        """Return the minimum value"""
        return min(self.data)
    
    def max(self):
        """Return the maximum value"""
        return max(self.data)
    
    def range(self):
        """Return the range (max - min)"""
        return self.max() - self.min()
    
    def mean(self):
        """Return the arithmetic mean"""
        return self.sum() / self.count()
    
    def median(self):
        """Return the median value"""
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        
        if n % 2 == 0:
            # Even number of elements - average of two middle values
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            # Odd number of elements - middle value
            return sorted_data[mid]
    
    def mode(self):
        """Return the mode (most frequent value)"""
        frequency = Counter(self.data)
        most_common = frequency.most_common(1)[0]
        return {'mode': most_common[0], 'count': most_common[1]}
    
    def var(self):  # ← Method name changed from 'variance' to 'var'
        """Return the variance"""
        mean_val = self.mean()
        squared_diff = sum((x - mean_val) ** 2 for x in self.data)
        return squared_diff / self.count()
    
    def std(self):
        """Return the standard deviation"""
        return math.sqrt(self.var())  # ← Now calling var() instead of variance()
    
    def freq_dist(self):
        """Return frequency distribution as percentage and value"""
        n = self.count()
        frequency = Counter(self.data)
        # Calculate percentage for each unique value, sort by value
        freq_dist_list = [(round((count / n) * 100, 1), value) 
                          for value, count in sorted(frequency.items())]
        return freq_dist_list

# Test the Statistics class with the given data
if __name__ == "__main__":
    ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
    
    data = Statistics(ages)
    
    print("=" * 50)
    print("STATISTICS CALCULATOR")
    print("=" * 50)
    print(f'Count: {data.count()}')
    print(f'Sum: {data.sum()}')
    print(f'Min: {data.min()}')
    print(f'Max: {data.max()}')
    print(f'Range: {data.range()}')
    print(f'Mean: {data.mean():.2f}')
    print(f'Median: {data.median()}')
    print(f'Mode: {data.mode()}')
    print(f'Standard Deviation: {data.std():.1f}')
    print(f'Variance: {data.var():.1f}')  # ← Now works with var() method
    print(f'Frequency Distribution: {data.freq_dist()}')