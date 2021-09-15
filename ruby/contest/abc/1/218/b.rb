P = gets.split(" ").map { |p| p.to_i }
P.each do |p|
  print ("a".."z").to_a[p-1]
end
puts