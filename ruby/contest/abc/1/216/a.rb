x, y = gets.split(".").map { |i| i.to_i }
if 0 <= y && y <= 2
  puts "#{x}-"
elsif 3 <= y && y <= 6
  puts x
else
  puts "#{x}+"
end
