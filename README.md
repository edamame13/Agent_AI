# 🧠 Agent_AI

OpenAI APIを使って動作する、**シンプルなCLI対話型AIエージェント**です。  
ターミナルから直接AIと会話できます。

### 1️⃣ リポジトリをクローン

```bash
git clone https://github.com/あなたのユーザー名/Agent_AI.git
cd Agent_AI

2️⃣ 仮想環境を作成して有効化

python3 -m venv venv
source venv/bin/activate   # macOS / Linux
# Windows の場合: venv\Scripts\activate

3️⃣ 依存パッケージをインストール

pip install openai


⸻

🔑 OpenAI APIキーの設定

OpenAIの APIキー管理ページ￼ から
APIキーを発行して、環境変数に設定します。

export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"

※このキーは 絶対にGitHubに公開しないでください！

⸻

💬 使い方

▶ 対話モードを開始

python openai_cli_agent.py

実行すると以下のように対話できます👇

=== 対話モード開始 ===
終了するには 'exit' または 'quit' と入力してください。
----------------------
あなた> こんにちは
AI> こんにちは！どうされましたか？
あなた> 今日の天気は？
AI> 申し訳ありませんが、リアルタイム天気情報は取得できません。


⸻

⚙️ 便利なエイリアス設定（任意）

毎回 source venv/bin/activate や python openai_cli_agent.py を打つのが面倒な場合、
.zshrc に以下を追記すると便利です。

# ~/.zshrc に追加
alias agent='cd ~/devlop/Agent_AI && source venv/bin/activate && python openai_cli_agent.py'

反映後：

source ~/.zshrc

これで次からは以下のコマンドだけで起動できます👇

agent


⸻

🧩 ファイル構成

Agent_AI/
├── openai_cli_agent.py   # メインのAIスクリプト
├── .gitignore            # 仮想環境や秘密情報を除外
├── README.md             # この説明書
└── venv/                 # 仮想環境（Git管理外）


⸻

⚠️ 注意事項
	•	APIキー (OPENAI_API_KEY) は 絶対にGitHubに公開しないでください。
	•	.zshrc や .env ファイルには個人情報が含まれる可能性があります。
.gitignore で除外することを推奨します。

⸻

🧠 使用モデル

デフォルトで以下のモデルを使用しています：

model="gpt-4o"

必要に応じて gpt-4-turbo などに変更可能です。