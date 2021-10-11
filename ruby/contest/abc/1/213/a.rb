a, b = gets.split(" ").map {|i| i.to_i}
(0...255).each do |c|
  if !!a ^ !!c
    puts c
    exit
  end
end
