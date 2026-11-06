from ...models import Post
from ..client import ContentClient

def _build_prompt(post_content):
    
    return (
        "Please provide a concise summary of the following blog post content. "
        "The summary must not exceed 500 characters:\n\n"
        f"{post_content}"
    )

def summarize_post(post_id):

    if not isinstance(post_id, int) or post_id <= 0:
        raise ValueError("Invalid post ID. Must be a positive integer.")

    # Retrieve the post & Handle missing posts
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise ValueError(f"Blog post with ID {post_id} does not exist.")

    # Validate the content
    if not post.content or not post.content.strip():
        raise ValueError("Cannot summarize a post with empty content.")

    #  AI processing
    prompt = _build_prompt(post.content)
    client = ContentClient()
    raw_summary = client.generate(prompt)

    # Validate the AI output
    if not raw_summary or not raw_summary.strip():
        raise ValueError("AI returned an empty summary.")
        
    cleaned_summary = raw_summary.strip()
    
    if len(cleaned_summary) > 500:
        cleaned_summary = cleaned_summary[:500]

        return {
        "post_id": post.pk,
        "title": post.title,
        "summary": cleaned_summary,
        "length": len(cleaned_summary)
    }