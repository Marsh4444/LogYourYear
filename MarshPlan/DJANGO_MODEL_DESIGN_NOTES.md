# Django Model Design Learning Guide

**Quick Reference for Designing Django Models - Beginner to Developer**

---

## **What is a Model?**

A model is a Python class that represents a database table. Each field = a column in the database.

---

## **The Todo Model Fields & Why I Chose Them:**

| Field | Type | Why This Choice |
|-------|------|-----------------|
| `title` | CharField(max_length=200) | **Essential** - Every todo needs a name. CharField for short text. max_length prevents huge entries. |
| `description` | TextField(blank=True, null=True) | **Optional** - Users might want details. TextField for longer text. blank=True = form can be empty. null=True = database can store NULL. |
| `completed` | BooleanField(default=False) | **Essential** - Tracks if todo is done. Boolean = simple True/False. default=False = new todos start incomplete. |
| `created_at` | DateTimeField(auto_now_add=True) | **Audit Trail** - Know when it was created. auto_now_add=True = automatically sets on creation (can't be changed). |
| `updated_at` | DateTimeField(auto_now=True) | **Audit Trail** - Know when it was last modified. auto_now=True = automatically updates every time you save. |
| `due_date` | DateTimeField(blank=True, null=True) | **Optional Feature** - Users might set deadlines. Optional because not all todos have due dates. |

---

## **Key Concepts to Remember:**

### **1. Required vs Optional Fields**

```python
# Required - must have value
title = models.CharField(max_length=200)  # No blank=True, no null=True

# Optional - can be empty
description = models.TextField(blank=True, null=True)  # Can skip in form & database
```

### **2. Field Types Matter**

```python
CharField       → Short text (titles, names) - specify max_length
TextField       → Long text (descriptions, content)
BooleanField    → True/False (flags, status)
DateTimeField   → Date + Time (timestamps, deadlines)
IntegerField    → Numbers (counts, ages)
EmailField      → Email validation built-in
URLField        → URL validation built-in
ImageField      → Image uploads
FileField       → File uploads
```

### **3. Auto Fields (Set Automatically)**

```python
auto_now_add=True   → Sets value ONCE when created (never changes again)
auto_now=True       → Updates EVERY time the object is saved
```

**Use Case:**
```python
created_at = models.DateTimeField(auto_now_add=True)  # Immutable - set once
updated_at = models.DateTimeField(auto_now=True)      # Changes every save
```

### **4. Audit Trail Fields (Best Practice)**

```python
# Always include these for tracking
created_at = models.DateTimeField(auto_now_add=True)  # When was it created?
updated_at = models.DateTimeField(auto_now=True)      # When was it last changed?
```

---

## **Things to Consider When Designing Any Model:**

| Question | Answer for Todo | General Principle |
|----------|-----------------|-------------------|
| **What's essential?** | title, completed | Core functionality |
| **What's optional?** | description, due_date | User convenience |
| **Need to track changes?** | Yes → add created_at, updated_at | Good practice |
| **Need validation?** | Yes → max_length on title | Data integrity |
| **What about relationships?** | Could add: user (ForeignKey) | Think about connections |
| **Future scalability?** | Keep fields flexible | Don't over-engineer |
| **Database performance?** | Use indexes on frequently queried fields | Optimize queries |

---

## **Why This Design is Good:**

✅ **Minimal but complete** - Has everything needed, nothing extra  
✅ **Flexible** - Optional fields allow different todo types  
✅ **Trackable** - Timestamps let you audit changes  
✅ **Scalable** - Easy to add user relationship later  
✅ **User-friendly** - Supports real-world use (due dates matter!)

---

## **What I DIDN'T Include (And Why):**

```python
# Could add but not necessary for basic app:
priority = models.IntegerField()        # Would add priority levels
user = models.ForeignKey(User, ...)     # For multi-user app
tags = models.ManyToMany(Tag)          # For categorization
reminder_email = models.BooleanField()  # For notifications
```

These aren't needed for MVP (minimum viable product) but could be added later.

---

## **Quick Decision Framework:**

When adding a field to ANY model, ask yourself:

1. **Is it necessary for the core function?** → Required field
2. **Will most users use it?** → Required field
3. **Will only some users use it?** → Optional field (blank=True, null=True)
4. **Is it metadata/tracking?** → Auto field (auto_now, auto_now_add)
5. **Might it change?** → Don't use auto_now_add, use auto_now instead

---

## **Field Options Explained:**

```python
# Common options you'll use:

max_length=200              # Maximum characters allowed (CharField only)
blank=True                  # Form can be left empty (front-end validation)
null=True                   # Database can store NULL (back-end validation)
default=False               # Default value if not provided
auto_now_add=True           # Auto-set on creation (immutable after)
auto_now=True               # Auto-update every save
editable=False              # User can't edit in forms
verbose_name="Custom Name"  # Human-readable name
help_text="Help message"    # Helpful text in forms
unique=True                 # Value must be unique across all records
db_index=True               # Create database index (faster queries)
on_delete=models.CASCADE    # What to do if related record deleted
```

---

## **Common Field Types Reference:**

```python
# Text Fields
models.CharField(max_length=100)     # Short text (required)
models.TextField()                   # Long text (required)
models.SlugField(max_length=50)      # URL-safe slug

# Numbers
models.IntegerField()                # Whole numbers
models.FloatField()                  # Decimal numbers
models.DecimalField(max_digits=10, decimal_places=2)  # Money

# Date/Time
models.DateField()                   # Date only (YYYY-MM-DD)
models.TimeField()                   # Time only (HH:MM:SS)
models.DateTimeField()               # Date + Time

# Boolean & Choice
models.BooleanField()                # True/False
models.BooleanField(null=True)       # True/False/Null

# Relationships
models.ForeignKey(OtherModel, on_delete=models.CASCADE)  # One-to-Many
models.ManyToManyField(OtherModel)                       # Many-to-Many
models.OneToOneField(OtherModel, on_delete=models.CASCADE)  # One-to-One

# Files & Media
models.ImageField(upload_to='images/')   # Image upload
models.FileField(upload_to='files/')     # File upload

# Others
models.EmailField()                  # Email with validation
models.URLField()                    # URL with validation
models.JSONField()                   # Store JSON data
```

---

## **The Todo Model in Plain English:**

*"A Todo is a thing someone wants to do. It has a title (required) and optionally a description. Users can mark it complete or incomplete. We track when it was made and when it changed. Users can optionally set a due date. Newest todos appear first."*

---

## **Model Design Checklist:**

Before saving your model, ask:

- [ ] Have I identified required vs optional fields?
- [ ] Do I have audit trail fields (created_at, updated_at)?
- [ ] Are my field names clear and descriptive?
- [ ] Have I used the right field type for each data?
- [ ] Is my model normalized (no duplicate data)?
- [ ] Can I easily query what I need?
- [ ] Have I added validation (max_length, choices)?
- [ ] Am I over-engineering it?

---

## **Migration Workflow:**

After changing a model:

```bash
python manage.py makemigrations   # Creates migration file
python manage.py migrate          # Applies to database
```

**Note:** Migrations track all changes so your database stays in sync with code.

---

## **Key Takeaway:**

**Focus on: Essential data + Optional convenience + Audit trails + Future flexibility**

Design models for the user's needs, not for features you might add someday. Keep it simple, document it, and scale when needed.

---

## **Learning Path:**

1. ✅ **Basic Models** - Simple fields (CharField, BooleanField, DateTimeField)
2. Next: **Relationships** - ForeignKey, ManyToMany
3. Next: **Validation** - Custom validators, signals
4. Next: **Performance** - Indexes, select_related, prefetch_related

---

**Remember:** A good model is the foundation of a good app. Take time to design it right! 🚀
