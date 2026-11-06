from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.ai_content.service import summarize_post


@api_view(["POST"])
def summarize_post_view(request, post_id):
    

    try:
        # calling the summarize_post function from the service layer
        result = summarize_post(post_id)
    
        return Response(result, status=status.HTTP_200_OK)
        
    except ValueError as exc:
        return Response({"error": str(exc)}, status=status.HTTP_400_BAD_REQUEST)