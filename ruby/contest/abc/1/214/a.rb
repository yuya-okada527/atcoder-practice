N = gets.to_i
if 1 <= N && N <= 125
  puts 4
elsif 126 <= N && N <= 211
  puts 6
else
  puts 8
end
