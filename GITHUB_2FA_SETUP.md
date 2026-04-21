# GitHub 2FA Authentication Setup Guide

Since your GitHub account is protected with 2-step authentication using an authenticator app, you'll need to use a Personal Access Token (PAT) instead of your password for git operations.

## Step 1: Create a Personal Access Token

1. Log in to your GitHub account
2. Click your profile picture in the top-right corner
3. Click "Settings"
4. In the left sidebar, click "Developer settings"
5. Click "Personal access tokens" → "Tokens (classic)"
6. Click "Generate new token" → "Generate new token (classic)"

**Token Settings:**
- **Note**: Enter "Code Library GUI" (or any descriptive name)
- **Expiration**: Choose "No expiration" or set a date
- **Scopes**: Select the following scopes:
  - ✅ `repo` (Full control of private repositories)
  - ✅ `workflow` (Update GitHub Action workflows)
  - ✅ `delete_repo` (Delete repos - optional)
  - ✅ `admin:org` (Admin org - optional)

7. Click "Generate token"
8. **IMPORTANT**: Copy the token immediately - you won't see it again!

## Step 2: Configure Git to Use the Token

### Option A: Use Token as Password (Recommended for Testing)

When prompted for a password during git operations, paste your Personal Access Token instead of your GitHub password.

### Option B: Store Token in Git Credential Helper (For Convenience)

```bash
# Configure git to store credentials
git config --global credential.helper store

# When you push next time, use the token as password
# It will be stored for future use
```

### Option C: Use Token in Remote URL (For Single Repository)

Replace your password in the URL with the token:

```bash
git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/code-library-gui.git
```

## Step 3: Test the Push

### Create a Test Repository First

Before pushing your main project, let's test with a simple command:

```bash
# Check current remote
git remote -v

# If no remote is set, add it:
git remote add origin https://github.com/YOUR_USERNAME/code-library-gui.git
```

### Push to GitHub

```bash
# Rename branch to main (if not already)
git branch -M main

# Push to GitHub
git push -u origin main
```

**When prompted for username:** Enter your GitHub username
**When prompted for password:** Paste your Personal Access Token

## Step 4: Verify the Upload

1. Go to your GitHub repository
2. Check that all files are present
3. Verify the commit message appears correctly
4. Check that README.md displays properly

## Troubleshooting

**"Authentication Failed" Error:**
- Verify your token has the correct scopes
- Ensure the token hasn't expired
- Check that you're using the token as password, not your GitHub password

**"Permission Denied" Error:**
- Ensure you have write access to the repository
- Verify the repository exists on GitHub
- Check that the remote URL is correct

**"Invalid Credentials" Error:**
- Make sure you're pasting the entire token
- Check for extra spaces or characters
- Regenerate the token if needed

## Security Best Practices

- **Never commit your token** to version control
- **Use different tokens** for different projects
- **Rotate tokens regularly** - delete old ones and create new ones
- **Limit token scopes** - only grant necessary permissions
- **Revoke unused tokens** - clean up tokens you no longer need

## Alternative: GitHub CLI (gh)

For a more modern approach, consider installing GitHub CLI:

```bash
# Install GitHub CLI
# Ubuntu/Debian:
sudo apt install gh

# Authenticate with 2FA:
gh auth login

# This will prompt for your GitHub credentials
# and handle 2FA automatically
```

Then you can push using:
```bash
gh repo create code-library-gui --public --source=.
git push -u origin main
```

## Next Steps

Once authenticated successfully:
- Your code will be on GitHub
- You can manage the repository through the GitHub web interface
- Others can clone and contribute to your project
- You can enable additional GitHub features (Issues, Actions, etc.)

---

**Remember:** Your Personal Access Token is like a password - keep it secure and never share it!
