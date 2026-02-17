#!/usr/bin/env python3
import argparse

def calculate_free_energy(survival, growth, impact=0, transcendence=0):
    return 10 * survival + 5 * growth + 0 * impact + 1 * transcendence

def main():
    parser = argparse.ArgumentParser(description="coco-toolkit Gap Calculator")
    parser.add_argument("--survival", type=int, required=True)
    parser.add_argument("--growth", type=int, required=True)
    parser.add_argument("--impact", type=int, default=0)
    parser.add_argument("--transcendence", type=int, default=0)
    args = parser.parse_args()
    
    F = calculate_free_energy(
        args.survival,
        args.growth,
        args.impact,
        args.transcendence
    )
    
    print(f"🧮 F = 10×{args.survival} + 5×{args.growth} + 0×{args.impact} + 1×{args.transcendence} = {F}")
    if F > 0:
        print("🔥 F > 0 → Driven!")
    else:
        print("⚠️  F = 0 → Warning: Don't coast!")

if __name__ == "__main__":
    main()

