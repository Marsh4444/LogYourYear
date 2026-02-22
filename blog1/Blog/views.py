from django.shortcuts import render, get_object_or_404, redirect
from bloggss.models import Blog
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from users.decorators import group_required
from .form import BlogForm
from django.utils.text import slugify
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Count
from django.contrib.auth.models import User



def home(request):
    """ Logic for the home page"""

    featured_posts = Blog.objects.filter(is_featured=True, status='published').order_by('-updated_at')
    blogs = Blog.objects.filter(status='published', is_featured=False).order_by('-updated_at')
    context = {
        'featured_posts': featured_posts,
        'blogs': blogs,
    }

    return render(request, 'home.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_desc__icontains=keyword) | Q(content__icontains=keyword)).order_by('-updated_at')

    context = {
        'keyword': keyword,
        'blogs' : blogs,
    }
    return render(request, 'search.html', context)

#post CRUD views will be in users/views.py since they are only for authenticated users/im using here cos the users view is clustered 






@login_required
def posts_list(request):
    if request.user.groups.filter(name="Manager").exists():
        posts = Blog.objects.all()
    else:
        posts = Blog.objects.filter(author=request.user)

    context = {
        'posts': posts
    }

    return render(request, 'posts/posts_list.html', context)





@login_required
@group_required("Manager", "Editor")  # only Managers and Editors
def posts_list(request):
    blogs = Blog.objects.all().order_by('-updated_at')  # fetch all blogs ordered by updated_at descending
    context = {"blogs": blogs}
    return render(request, "users/dashboard/posts_list.html", context)



@login_required
@group_required("Manager", "Editor")  # adjust role if needed
def post_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        
        if form.is_valid():
            blog = form.save(commit=False)

            # Assign author automatically
            blog.author = request.user

            blog.save()  # Save first to generate ID

            # Generate unique slug using ID
            blog.slug = slugify(blog.title) + "-" + str(blog.id)
            blog.save()

            return redirect("posts_list")
        else:
            print("Form is not valid:")
            print(form.errors)
    else:
        form = BlogForm()

    context = {
        "form": form
    }

    return render(request, "users/dashboard/posts_create.html", context)


@login_required
@group_required("Manager", "Editor")  # adjust if Editors can edit too
def post_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            updated_blog = form.save(commit=False)

            # Optional: regenerate slug if title changed
            if "title" in form.changed_data:
                updated_blog.slug = slugify(updated_blog.title) + "-" + str(updated_blog.id)

            updated_blog.save()

            return redirect("posts_list")
    else:
        form = BlogForm(instance=blog)

    context = {
        "form": form,
        "blog": blog
    }

    return render(request, "users/dashboard/posts_update.html", context)


def post_delete(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts_list')


@login_required
@group_required("Manager", "Editor")  # only Managers and Editors
def system_reports(request):
    # ----- Summary Stats -----
    total_blogs = Blog.objects.count()
    recent_blogs = Blog.objects.order_by("-created_at")[:5]

    one_month_ago = now() - timedelta(days=30)
    blogs_this_month = Blog.objects.filter(created_at__gte=one_month_ago).count()

    total_users = User.objects.count()
    total_managers = User.objects.filter(groups__name="Manager").count()
    total_editors = User.objects.filter(groups__name="Editor").count()
    total_authors = User.objects.filter(groups__name="Author").count()

    most_active_author = (
        Blog.objects.values("author__username")
        .annotate(post_count=Count("id"))
        .order_by("-post_count")
        .first()
    )

    # ----- Chart Data -----
    # 1. Blogs per Category
    blogs_per_category = (
        Blog.objects.values("category__category_name")
        .annotate(count=Count("id"))
        .order_by("-count")
    )
    category_labels = [b["category__category_name"] for b in blogs_per_category]
    category_counts = [b["count"] for b in blogs_per_category]

    # 2. Role Distribution
    role_counts = {
        "Managers": total_managers,
        "Editors": total_editors,
        "Authors": total_authors,
    }
    role_labels = list(role_counts.keys())
    role_data = list(role_counts.values())

    # 3. Monthly Blog Growth (last 6 months)
    monthly_labels = []
    monthly_data = []
    for i in range(5, -1, -1):  # last 6 months
        month = now() - timedelta(days=i*30)
        monthly_labels.append(month.strftime("%b %Y"))
        count = Blog.objects.filter(
            created_at__year=month.year, created_at__month=month.month
        ).count()
        monthly_data.append(count)

    context = {
        "total_blogs": total_blogs,
        "blogs_this_month": blogs_this_month,
        "recent_blogs": recent_blogs,
        "total_users": total_users,
        "total_managers": total_managers,
        "total_editors": total_editors,
        "total_authors": total_authors,
        "most_active_author": most_active_author,
        "category_labels": category_labels,
        "category_counts": category_counts,
        "role_labels": role_labels,
        "role_data": role_data,
        "monthly_labels": monthly_labels,
        "monthly_data": monthly_data,
    }

    return render(request, "users/dashboard/system_reports.html", context)