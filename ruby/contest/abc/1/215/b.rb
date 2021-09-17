N = gets.to_i
k = 1
while 2**k <= N
  k += 1
end
puts k-1