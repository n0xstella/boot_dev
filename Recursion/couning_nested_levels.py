def count_nested_levels(nested_documents, target_document_id, level=1):
    for doc_id, sub_docs in nested_documents.items():
        if doc_id == target_document_id:
            return level

        if isinstance(sub_docs, dict):
            result = count_nested_levels(sub_docs, target_document_id, level + 1)    
            if result != -1:
                return result     
    
    return -1