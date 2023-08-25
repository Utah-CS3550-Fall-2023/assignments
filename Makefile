.PHONY: screenshots

screenshots:
	mkdir -p screenshots
	sh infra/screenshot.sh "" screenshots/assignments.png
	sh infra/screenshot.sh 2 screenshots/assignment.png
	sh infra/screenshot.sh 2/grade screenshots/submissions.png
	sh infra/screenshot.sh profile screenshots/profile.png
	sh infra/screenshot.sh profile/login screenshots/login.png
