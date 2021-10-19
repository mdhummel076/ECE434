# Hw 6 #

Cyclictest.png holds the image file for the timing results. As you can see from the plot, the rt kernel performs better than the non-rt kernel.
However, the high load tests are both worse than the low load tests. The high load tests were done by toggling a gpio pin as fast as possible, putting CPU usage at 100%.

The highest recorded latency for the rt-kernel is ~225us, while the non-rt kernel maxxed out at ~490us.
