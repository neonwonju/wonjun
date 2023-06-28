# 숫자 야구 게임 코드

def generate_random_numbers(digits)
  (0..9).to_a.sample(digits).join
end

def get_user_input(digits)
  print "3자리 숫자를 입력하세요: "
  input = gets.chomp

  # 입력값 확인 및 유효성 검사
  until input.length == digits && input.chars.uniq.length == digits && input =~ /^[0-9]+$/
    print "틀렸습니다. 다시 3자리 숫자를 입력하세요: "
    input = gets.chomp
  end

  input
end

def check_guess(user_input, target_numbers)
  strike, ball = 0, 0

  user_input.chars.each_with_index do |num, idx|
    if target_numbers.include?(num)
      num == target_numbers[idx] ? strike += 1 : ball += 1
    end
  end
  return strike, ball
end

def number_baseball_game
  digits = 3
  target_numbers = generate_random_numbers(digits)
  attempts = 0
  user_input = ""

  puts "숫자 야구 게임을 시작합니다!"
  puts "숫자 야구 게임에서는 1부터 9까지의 숫자 중 중복 없이 3개의 숫자를 추측해야 합니다."

  while user_input != target_numbers
    user_input = get_user_input(digits)
    strike, ball = check_guess(user_input, target_numbers)
    attempts += 1

    puts "스트라이크: #{strike}, 볼: #{ball}"
    break if strike == digits
  end

  puts "축하합니다! 당신은 숫자 #{target_numbers}를 맞췄습니다!"
  puts "총 시도 횟수: #{attempts}번"
end

number_baseball_game
