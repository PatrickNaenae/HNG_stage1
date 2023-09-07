from rest_framework import serializers

class InfoSerializer(serializers.Serializer):
    slack_name = serializers.CharField(
        max_length=200, 
        help_text="Name on Slack"
    )
    current_day = serializers.CharField(
        max_length=200, 
        help_text="Current day of the week"
    )
    utc_time = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%SZ", 
        help_text="Current UTC time"
    )
    track = serializers.CharField(
        max_length=200, 
        help_text="User's track"
    )
    github_file_url = serializers.CharField(
        max_length=200, 
        help_text="URL of the file being run on GitHub"
    )
    github_repo_url = serializers.CharField(
        max_length=200, 
        help_text="URL of the full source code on GitHub"
    )
    status_code = serializers.IntegerField(
        min_value=200, 
        max_value=299, 
        help_text="HTTP status code"
    )

