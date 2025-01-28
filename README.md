<p align="center">
    <h1 align="center">Classroom by adimail</h1>
</p>

### Get Involved

Static site with a collection of notes from [my](https://adimail.github.io/) BTech.

## Run locally

Before you begin, ensure you have the following installed:
- Ruby (version 3.0.0 or higher)
- RubyGems
- Bundler
- Git

#### macOS
```bash
brew install rbenv
rbenv init
rbenv install 3.2.0
rbenv global 3.2.0
```

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev libreadline-dev zlib1g-dev
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/main/bin/rbenv-installer | bash
rbenv install 3.2.0
rbenv global 3.2.0
```

#### Windows
Download and install Ruby using the [RubyInstaller](https://rubyinstaller.org/).

### 4. Install Bundler

After installing Ruby, install Bundler:
```bash
gem install bundler
```

### 5. Install Project Dependencies

```bash
bundle install
```

### 6. Run the Project

```bash
bundle exec jekyll serve
```

Open your web browser and navigate to `http://localhost:4000` to see the Jekyll site in action.
