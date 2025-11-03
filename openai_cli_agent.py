#!/usr/bin/env python3
import os
from openai import OpenAI

def make_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY が設定されていません。環境変数を確認してください。")
    return OpenAI(api_key=api_key)

def main():
    client = make_client()
    print("=== 対話モード開始 ===")
    print("終了するには 'exit' または 'quit' と入力してください。")
    print("----------------------")

    # 会話履歴を保持（文脈を維持する）
    messages = [
        {"role": "system", "content": "あなたは親切なアシスタントです。短く端的に答えてください。"}
    ]

    while True:
        user_input = input("あなた> ").strip()
        if user_input.lower() in ["exit", "quit", "終了"]:
            print("AI> さようなら！")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=300
            )
            reply = response.choices[0].message.content
            print("AI>", reply)
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print("⚠️ エラー:", e)
            break

if __name__ == "__main__":
    main()