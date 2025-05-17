def math_calculator():
    print("\n🧮 Math Calculator")
    expr = input("Enter a math expression (e.g., 2+3*4): ")
    try:
        result = eval(expr)
        print(f"✅ Result: {result}")
    except:
        print("❌ Error: Invalid expression")

def badminton_guide():
    print("\n🏸 Badminton Tips:")
    print("- Grip: Learn how to hold the racket properly.")
    print("- Footwork: Move quickly and stay balanced.")
    print("- Smashes & Clears: Practice powerful and accurate shots.")
    print("🎥 Video guide: Watch 'badminton_tips.mp4' in your video player.")

def other_sports_guide():
    print("\n⚽ Other Sports Tips:")
    print("Football:")
    print("- Practice dribbling, passing, and shooting accurately.")
    print("Basketball:")
    print("- Work on shooting form, defense, and teamwork.")
    print("🎥 Video guide: Watch 'multisport_tips.mp4' in your video player.")

def main_menu():
    while True:
        print("\n📋 MAIN MENU:")
        print("1. Math Calculator")
        print("2. Badminton Tips")
        print("3. Other Sports Tips")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == '1':
            math_calculator()
        elif choice == '2':
            badminton_guide()
        elif choice == '3':
            other_sports_guide()
        elif choice == '4':
            print("👋 Exiting. Have a great day!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
