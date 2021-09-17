S, T = gets.split(" ").map { |s| s.to_i }
ans = 0
(0..S).each do |a|
  (0..S).each do |b|
    (0..S).each do |c|
      ans += a + b + c <= S && a * b * c <= T ? 1 : 0
    end
  end
end
puts ans
